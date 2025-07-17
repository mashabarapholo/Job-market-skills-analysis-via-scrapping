# Job Market Skills Analysis via Web Scraping

## Project Overview

This project scrapes Python job postings from python.org/jobs, extracts the full text of each description, and analyzes the text to identify the most in-demand technical skills. The entire workflow is built with Python, showcasing skills in web scraping, data cleaning, text analysis, and data visualization.

## Key Features

- **Deep Web Scraping:** A two-phase scraper built with `requests` and `BeautifulSoup` first gathers job links and then visits each link to extract the full description.
- **Text Analysis & NLP:** Uses Python's `re` module (regular expressions) to search for a pre-defined dictionary of technical keywords and aliases (e.g., "AWS", "SQL", "Django") within the unstructured text of job descriptions.
- **Data Aggregation:** Leverages the `pandas` library to structure the scraped data and aggregate the skill counts into a final report.
- **Data Visualization:** Generates a professional bar chart with `Matplotlib` and `Seaborn` to visually represent the frequency of each skill, providing a clear answer to the project's main question.

## Final Result: Most In-Demand Skills

The analysis produced the following chart, highlighting the technical skills most frequently mentioned in the job postings. This provides actionable intelligence for job seekers looking to align their skills with market demand.

![Skill Demand Chart]

<img width="1200" height="1000" alt="skill_demand_chart" src="https://github.com/user-attachments/assets/6db47254-9fa7-4370-bf1e-1e46329eb3c7" />


## Tech Stack

- **Language:** Python
- **Libraries:**
    - **requests & BeautifulSoup4:** For web scraping.
    - **pandas:** For data manipulation and structuring.
    - **re (Regular Expressions):** For pattern matching in text.
    - **Matplotlib & Seaborn:** For data visualization.
- **Environment:** Jupyter Notebook / Python Script

## How to Run

1.  Clone this repository: `git clone [your-repo-url]`
2.  Navigate to the project directory: `cd job_scraper_project`
3.  Create and activate a virtual environment.
4.  Install the required dependencies:
    ```bash
    pip install requests beautifulsoup4 pandas matplotlib seaborn
    ```
5.  Run the scraper to gather the latest data:
    ```bash
    python scraper.py
    ```
6.  Run the analysis script on the generated data:
    ```bash
    python analyzer.py
    ```
