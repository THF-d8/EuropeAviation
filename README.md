[<img src="https://img.shields.io/badge/License-MIT-yellow.svg"
alt="License:MIT" />](https://opensource.org/licenses/MIT)

# ✈️ EuropeAviation

## Welcome to the world of aviation

You are in the right place if you are a big fan of aviation, or to put it in simple words - a big fan of flying. In this app you will be able to explore the busiest airports in Europe and take a look at how many flights are flying in and out of those airports every month.

-   [Motivation](#motivation)
-   [Explore the app](#explore-the-app)
-   [Description](#description)
-   [About the data](#about-the-data)
-   [Usage](#usage)
-   [Contributing](#contributing)

## Motivation 

The aviation industry is an important component of modern transportation infrastructure, providing safe and efficient travel across distances. In Europe, the number of flights has been increasing steadily over the past decades, leading to significant challenges in terms of air traffic management and passenger experience. To address these challenges, it is necessary to analyze the available flight data and identify key trends and patterns that can inform more effective policies and strategies.

## Explore the app 

You can access the deployed app on [https://europeaviation.onrender.com](https://europeaviation.onrender.com/)

## Description 

The interactive dashboard includes three distinct components in the form of dropdown menus, allowing users to select the desired year (ranging from 2016 to 2022), the month of the year (between 1 and 12), and the flight type (departure, arrival, or both). Upon selection, users will be able to view an interactive bar chart displaying the top 10 busiest airports based on their selected flight type. The bar chart includes the name and ICAO code for each airport, and users can easily hover over each bar to examine the number of flights. Additionally, a line chart will be displayed showing three trend lines - the number of flights by departure, the number of flights by arrival, and the total number of flights - for the busiest airport during the selected month. Users can also examine the number of flights for each type on any given day of the selected month by hovering over each point on the line chart.

## About the data 

The data was collected from [Eurocontrol](https://ansperformance.eu/data/), including the data of flights information in Europe from January 1st, 2016 to May 5th, 2022. The dataset contains 688099 registers including daily number of departure flights, arrival flights and total number of flights for each airport in Europe.

The data set is public and can be found in [tidytuesday](https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-07-12). Follow this link to access to the source dataset [flights.csv](https://github.com/rfordatascience/tidytuesday/blob/master/data/2022/2022-07-12/flights.csv).

## Usage

To install `EuropeAviation` locally, you can do as follows:

1.  Clone this repository to your local directory.

2.  We have created an environment (euro_avia.yaml), using which our app can be reproduced locally. To create this environment locally, go to the root of this repository and run:

    ``` bash
    conda env create -f euro_avia.yaml
    ```

3.  Activate it by running:

        conda activate euro_avia

4.  In the src folder of this repository run the following command:

        python app.py

5.  Copy the address and paste it in your browser to load the dashboard.

## Contributing 

Interested in contributing? We are glad you are interested, please check out the [contributing guidelines](https://github.com/THF-d8/EuropeAviation/blob/main/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/THF-d8/EuropeAviation/blob/main/CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`EuropeAviation` was created by Crystal Geng. The materials of this project are licensed under the MIT License. If re-using/re-mixing please provide attribution and link to this webpage.
