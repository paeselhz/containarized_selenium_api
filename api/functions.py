from bs4 import BeautifulSoup
import pandas as pd

def return_population_by_country(selenium_driver,
                                 continent = None):

    selenium_driver.get("https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)")

    html_source = selenium_driver.page_source

    soup = BeautifulSoup(html_source, "html.parser")

    table_raw_html = soup.select_one("#mw-content-text > div.mw-parser-output > table")

    full_table = pd.read_html(str(table_raw_html))[0].rename(columns={"Country/Territory": "country",
                                                                      "UN continentalregion[4]": "continent",
                                                                      "UN statisticalsubregion[4]": "statistical_subregion",
                                                                      "Population(1 July 2018)": "population_2018",
                                                                      "Population(1 July 2019)": "population_2019",
                                                                      "Change": "change"})

    if continent is None:
        return_df = full_table[["country", "continent", "population_2018", "population_2019"]]
    else:
        return_df = full_table[full_table['continent'] == continent][
        ["country", "continent", "population_2018", "population_2019"]]

    return return_df
