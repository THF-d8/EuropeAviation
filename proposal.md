---
editor_options: 
  markdown: 
    wrap: sentence
---

# EuropeAviation project proposal

## Motivation and purpose

##### Target audience:

> Aviation enthusiasts who are passionate about flying and interested in discovering the busiest airports in Europe every month of the year, along with the number of departing and arriving flights at these airports.

##### Motivation:

> The aviation industry is an important component of modern transportation infrastructure, providing safe and efficient travel across distances.
> In Europe, the number of flights has been increasing steadily over the past decades, leading to significant challenges in terms of air traffic management and passenger experience.
> To address these challenges, it is necessary to analyze the available flight data and identify key trends and patterns that can inform more effective policies and strategies.

## Description of the data

The data was collected from [Eurocontrol](https://ansperformance.eu/data/), including the data of flights information in Europe from January 1st, 2016 to May 5th, 2022.
The dataset contains 688099 registers including daily number of departure flights, arrival flights and total number of flights for each airport in Europe.

The dataset is made up of 13 variables, both categorical and numerical, these variables represent attributes associated with the year, the month, the date, the airports and number of flights.
Below is a summary of the variables of the dataset:

| variable      | type     | description                                                   |
|:-----------------------|:-----------------------|:-----------------------|
| YEAR          | int      | Reference year                                                |
| MONTH_NUM     | int      | Month (numeric)                                               |
| MONTH_MON     | str      | Month (3-letter code)                                         |
| FLT_DATE      | datetime | Date of flight                                                |
| APT_ICAO      | str      | ICAO 4-letter airport designator                              |
| APT_NAME      | str      | Airport name                                                  |
| STATE_NAME    | str      | Name of the country where the airport is located at           |
| FLT_DEP_1     | int      | Number of IFR departures collected from Network Manager       |
| FLT_ARR_1     | int      | Number of IFR arrivals collected from Network Manager         |
| FLT_TOT_1     | int      | Number total IFR movements collected from Network Manager     |
| FLT_DEP_IFR_2 | int      | Number of IFR departures collected from Airport Operator      |
| FLT_ARR_IFR_2 | int      | Number of IFR arrivals collected from Airport Operator        |
| FLT_TOT_IFR_2 | int      | Number of total IFR movements collected from Airport Operator |

From the table it can be seen that there are flight data collected from two different sources: Network Manager and Airport Operator.
To ensure consistency and reduce the size of the dataset, we only select the data collected from the Network Manager.

Attribution:

> The data set is public and can be found in [tidytuesday](https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-07-12).
> Follow this link to access to the source dataset [flights.csv](https://github.com/rfordatascience/tidytuesday/blob/master/data/2022/2022-07-12/flights.csv).

## Research questions

The research questions of this study are about analyzing European flight data and identifying key insights that can help improve air travel efficiency.
Specifically, here are some of the questions that can be answered through the interaction with the dashboard:

-   What are the top 10 busiest airports in January 2017?

-   How many flights are arriving at the Amsterdam Schiphol (AMS) airport in June 2018?

-   How many flights are departing from the Charles de Gaulle Airport (CDG) in May 2019?

-   What is the busiest airport in January 2017?

-   For the busiest airport in January 2017, how many flights are departing from and arriving at this airport everyday?

## Usage scenario 

Considering our target audience, an example usage of our dashboard can be:

> Bonin recently got very interested in civil aviation.
> As a young and new flight enthusiast living in Paris, he wants to know the flight volume each day at each European airport since he travels within Europe very often.
> He is also interested in knowing which are the busiest airports in Europe in 2018.
> Although Bonin flies a lot, he has limited knowledge and does not know how to collect data about the airports.
> Coincidentally, Bonin found our dashboard where he is able to select the year and month he is interested in, then choose his preferred type of flight (departure or arrival).
> The dashboard is able to display a bar chart showing the top 10 busiest airports for the selected fight type, and Bonin can hover over each bar to examine the exact number of flights at that corresponding airport.
> After spending a fair amount of time playing with our dashboard, Bonin's interested in aviation is strengthened and decides to become a pilot at Air France.\

Another use case scenario can be:

> Way Ming is a data analyst working for a SilkAir.
> He is responsible for monitoring the performance of the company's European flights.
> Way Ming uses our Dashboard to gain insights into the busiest airports and flight types for a particular month and year.
> For example, he is able to simply open his web browser and selects the year 2021 and the month of August from the two dropdown menus, then he can select the "total" option as he wants to see the total number of flights for each airport.
> The bar chart updates to show the 10 busiest airports by the total number of flights in 2021.
> From the bar chart, Way Ming can see that the top three busiest airports are Amsterdam Schiphol (AMS) airport has the highest number of flights, followed by Istanbul Airport (IGA) and Paris Charles de Gaulle (CDG).
> Based on this finding, Way Ming can report to his team that AMS, IGA and CDG are the busiest airports in August 2021, and there were 33k, 31k and 29k total number of flights at these airports respectively.
> He can use this information to plan future flight schedules and allocate the airline's resource accordingly.
> Fascinated by how many flights are happening at these airports, Way Ming got very curious about how it would feel like to be able to constantly fly into and out of these airports.
> With this ambition in mind, Way Ming decides to switch gears to become a pilot at SilkAir.
