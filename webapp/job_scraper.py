from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape_data(job_search):
    global data
    df = pd.DataFrame(columns=['title', 'company', 'salary', 'link'])

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    url = f"https://www.jobs.cz/prace/praha/?q%5B%5D={job_search}"
    html_response = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_response.content, 'html.parser')

    job_grid = soup.find_all(class_='standalone search-list__item')


    for job in job_grid:
        try:
            title = job.find('a').text.strip()
            company = job.find(class_='search-list__secondary-info--label notranslate').text.strip()
            link = job.find(class_="search-list__main-info__title__link").get('href')
            try:
                salary = job.find(class_='search-list__tags__label search-list__tags__salary--label').text.strip()
            except AttributeError:
                salary = 'N/A'

            df = df.append({'title': title, 'company': company, 'salary': salary, 'link': link}, ignore_index=True)

        except AttributeError:
            pass

    data = df.iloc[1:].values
    return data
