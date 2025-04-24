# OLYMPICS DATA ANALYSIS
## About
Hey there! Welcome to the olumpics analysis. I develop this project as my **3rd semester python project**. This is my **first python project**. I'm excited to share it with you. This project is about data analysis and visulisation that uses a **pandas, plotly, seaborn and matplotlib** libraries as fundamental technology. This project include different types of analysis which can be used interactively from **streamlit web app**. For analysis i considered **summer season only** this has total 120 years of data(1896-2016).

What it includes?

1) **Medal Tally**

    -> year-wise

    -> country-wise

    -> overall

2) **Overall Analysis**

    -> includes useful maps

3) **Country-wise analysis**

    -> mainly includes charts and useful insights

First we will need to collect data about the movies for this use **120 years of Olympic history: athletes and results** [Visit Dataset](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results "Download or get more information about the dataset"). The flow of project is mainly divided into four parts: **data collection, data preprocessing, and creating website**.

## Installations
1. Clone the repo:
   ```sh
   git clone https://github.com/jainamb12/olympic-data-analysis.git
   ```
2. Install the required packages:
   ```sh
   pip install numpy pandas streamlit matplotlib seaborn plotly
   ```
3. Run the project using command:
   ```sh
   streamlit run app.py
   ``` 
   **NOTE** : In case the above command doesn't work, try running the file by giving absolute file path in your terminal:

## Logic
\* Filter the data by removing winter rows

\* Merge two datasets: athelete_events.csv and noc_regions.csv on basis of NOC. This will give us the complete information about the atheletes.

\* Preprocess the data or clean the dataset, then do **OHE** on medal column after that do **group by** on NOC basis sum the total medals **sort by gold**. But output is very different from expected when compare to real values from sources this is because data is *according to athelete not according to team* means india won gold in hocky in 1928 then total 11 gold medals will be consider for that particular year not 1 time
to solve this drop rows which has same values for **Team , NOC , Games , Year , City , Sport , Event , Medal** then group by again 

\* cover 4 different cases of filtering dataset by country and year, write same method in helper file .

**Note** : In above analysis results may slightly vary because of historical and geographical circumstances for that country e.g. russia, germany etc.

\* In overall analysis part first there is top statistics about olympics which is obtained by getting unique records from a particulat column and count it. after that there are plots and maps.

\* Finally for country wise analysis there is plot for it's medal tally and a map showing that country excels in which sports

## Features
1. User Input selection for preferences
2. Attractive UI using Streamlit
3. charts and maps for better visualisation
4. manages data properly for each analysis
5. Deployed on **streamlit cloud** for easy access

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the project.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
