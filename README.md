# How the Spread of COVID-19 Has Been Lowered by Quarantining
A report by Alec Barker on how quarantining and other protective measures have slowed the spread of COVID-19.

This project was created for PHY 299: Scientific Modelling & Data Analysis that was taught by Dr. Colin Campbell at the University of Mount Union.

## Features
Running the provided code will produce four graphs:
- The daily confirmed cases.
- The daily confirmed cases compared to the SIR model values (zoomed in).
- The daily confirmed cases compared to the SIR model values (zoomed out).
- The SIR model daily values.

Additionally, some statistics will be printed to the console, including:
- Number of confirmed infected individuals for the latest date.
- Number of infected individuals for the latest date according to the SIR model.
- Total length of the pandemic before COVID-19 dies off (less than one infected individual) according to the SIR model.
- Total number of infected individuals during the entire pandemic according to the SIR model.
- Total number of individuals that never get infected during the entire pandemic according to the SIR model.
- Peak number of individuals infected during a single day and the date of the peak according to the SIR model.

## Instructions
1. Install [Matplotlib](https://matplotlib.org/users/installing.html) and [SciPy](https://www.scipy.org/install.html).
2. Download the [daily situation update](https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases) from the ECDC website in CSV format.
3. Rename the CSV file as *covid19_data* and move it to the *Data Files* folder.
4. Run *data_scraper.py*.
5. Adjust data values in *covid19_sir.py* if needed.
6. Run *covid19_sir.py*.
