import collections
import datetime
import os

from http.server import HTTPServer, SimpleHTTPRequestHandler

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd

def format_year_answer(year):
    if year % 100 in (11, 12, 13, 14):
        return 'лет'
    if year % 10 == 1:
        return 'год'
    if year % 10 in (2, 3, 4):
        return 'года'
    return 'лет'


def get_categorized_wines(catalogue_path):
    wines = pd.read_excel(catalogue_path, keep_default_na=False).to_dict(orient='records')

    wines_by_categories = collections.defaultdict(list)
    for wine in wines:
        wines_by_categories[wine['Категория']].append(wine)
    wine_categories = sorted(wines_by_categories.items(), key=lambda x: x[0])
    wines_by_categories = dict(wine_categories)
    return wines_by_categories

if __name__ == '__main__':
    load_dotenv()
    wines_catalogue = os.getenv('WINES')

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    wines_by_categories = get_categorized_wines(wines_catalogue)

    winery_foundation_date = 1920
    winery_years_old = datetime.date.today().year - winery_foundation_date

    rendered_page = template.render(
        winery_years=f'Уже {winery_years_old} {format_year_answer(winery_years_old)} с вами!',
        wines_by_categories=wines_by_categories
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
