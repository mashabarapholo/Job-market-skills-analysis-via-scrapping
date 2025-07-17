# In scraper.py (Upgraded Version for Deep Scraping)

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time # Import the time library to add delays

def get_job_description(job_url):
    """
    Visits a specific job page URL and scrapes the full text of the job description.
    """
    try:
        page = requests.get(job_url)
        page.raise_for_status()
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # By inspecting the job description page, we find the main content
        # is within a <article> tag with the class "text".
        job_description_container = soup.find('article', class_='text')
        
        if job_description_container:
            return job_description_container.text.strip()
        else:
            return "Description not found."
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching job description from {job_url}: {e}")
        return "Could not retrieve description."


def scrape_python_jobs():
    """
    Main scraping function. Scrapes the list of jobs, then visits each
    job's page to get the full description.
    """
    URL = "https://www.python.org/jobs/"
    print(f"Scraping main job list from: {URL}")

    try:
        page = requests.get(URL)
        page.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find('ol', class_='list-recent-jobs')
    
    if not results:
        print("Could not find the job listing container.")
        return []

    job_elements = results.find_all('li')
    jobs_list = []
    
    print(f"Found {len(job_elements)} jobs. Now scraping individual descriptions...")
    
    for job_elem in job_elements:
        title_elem = job_elem.find('h2').find('a')
        company_elem = job_elem.find('span', class_='listing-company')
        job_type_elem = job_elem.find('span', class_='listing-job-type')
        date_elem = job_elem.find('time')

        title = title_elem.text.strip() if title_elem else "N/A"
        company = company_elem.text.strip() if company_elem else "N/A"
        job_type = job_type_elem.text.strip() if job_type_elem else "N/A"
        post_date = date_elem.text.strip() if date_elem else "N/A"
        
        link_url = title_elem['href'] if title_elem else None
        
        if link_url:
            full_link = f"https://www.python.org{link_url}"
            
            # --- THIS IS THE NEW PART ---
            # Call our new function to get the description
            print(f"-> Scraping description for: {title}")
            description = get_job_description(full_link)
            
            # Add a small delay to be a polite scraper
            time.sleep(1) # Wait for 1 second before the next request
        else:
            full_link = "N/A"
            description = "N/A"

        jobs_list.append({
            "Title": title,
            "Company": company,
            "Job Type": job_type,
            "Post Date": post_date,
            "Description": description, # Add the new description field
            "Link": full_link
        })
        
    return jobs_list


if __name__ == "__main__":
    scraped_jobs = scrape_python_jobs()
    
    if scraped_jobs:
        df = pd.DataFrame(scraped_jobs)
        df.to_csv('python_jobs_with_descriptions.csv', index=False)
        
        print(f"\nSuccessfully scraped {len(df)} full job descriptions.")
        print("Data saved to python_jobs_with_descriptions.csv")
        print("\n--- First 5 Jobs with Descriptions ---")
        print(df.head())
    else:
        print("Could not scrape any jobs.")