# In analyzer.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re # Import the regular expressions library

def analyze_job_skills(csv_file_path):
    """
    Reads a CSV file of job postings, analyzes the descriptions for
    pre-defined skills, and generates a visualization of the most
    in-demand skills.
    """
    
    # --- Step 1: Load the Data ---
    try:
        df = pd.read_csv(csv_file_path)
        # Drop rows where the description is missing, as we can't analyze them
        df.dropna(subset=['Description'], inplace=True)
        print(f"Successfully loaded and cleaned {len(df)} job postings.")
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
        return

    # --- Step 2: Define the Dictionary of Skills ---
    # We can add more skills or aliases here easily.
    # The key is the "clean" name of the skill.
    # The value is a list of patterns to search for. We use '\b' for word boundaries
    # to avoid matching "React" inside "Reaction", for example.
    skills_dict = {
        'Python': [r'\bpython\b'],
        'Django': [r'\bdjango\b'],
        'Flask': [r'\bflask\b'],
        'SQL': [r'\bsql\b'],
        'PostgreSQL': [r'\bpostgresql\b', r'\bpostgres\b'],
        'MySQL': [r'\bmysql\b'],
        'AWS': [r'\baws\b', r'amazon web services'],
        'Azure': [r'\bazure\b'],
        'GCP': [r'\bgcp\b', r'google cloud'],
        'Docker': [r'\bdocker\b'],
        'Kubernetes': [r'\bkubernetes\b', r'\bk8s\b'],
        'Git': [r'\bgit\b'],
        'React': [r'\breact\b'],
        'JavaScript': [r'\bjavascript\b', r'\bjs\b'],
        'HTML/CSS': [r'\bhtml\b', r'\bcss\b'],
        'Machine Learning': [r'machine learning', r'\bml\b'],
        'AI': [r'\bai\b', r'artificial intelligence']
    }

    # --- Step 3: Analyze Each Description for Skills ---
    # Initialize a dictionary to hold the counts of each skill
    skill_counts = {skill: 0 for skill in skills_dict.keys()}

    for description in df['Description']:
        # We process each description only once
        description_lower = description.lower() # Convert to lowercase for case-insensitive matching
        
        # For each skill in our dictionary...
        for skill, patterns in skills_dict.items():
            # Check if any of the patterns for that skill appear in the description
            is_skill_present = any(re.search(pattern, description_lower) for pattern in patterns)
            if is_skill_present:
                # If the skill is found, increment its count.
                # We only count each skill once per job to find out how many jobs require a skill.
                skill_counts[skill] += 1
    
    # --- Step 4: Prepare Data for Visualization ---
    # Convert the counts dictionary to a pandas DataFrame for easy plotting
    skills_df = pd.DataFrame(list(skill_counts.items()), columns=['Skill', 'Count'])
    
    # Sort the skills by count in descending order
    skills_df = skills_df.sort_values(by='Count', ascending=False).reset_index(drop=True)
    
    print("\n--- Skill Analysis Complete ---")
    print(skills_df)
    
    # --- Step 5: Visualize the Results ---
    plt.figure(figsize=(12, 10))
    
    # Create a horizontal bar plot for better readability of skill names
    sns.barplot(x='Count', y='Skill', data=skills_df, palette='viridis')
    
    plt.title('Most In-Demand Skills for Python Jobs', fontsize=18)
    plt.xlabel('Number of Job Postings Mentioning Skill', fontsize=14)
    plt.ylabel('Technical Skill', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    # Ensure layout is tight so everything fits
    plt.tight_layout()
    
    # Save the plot to a file
    plt.savefig('skill_demand_chart.png')
    
    print("\nChart has been saved as 'skill_demand_chart.png'")
    
    plt.show()


# --- Main execution block ---
if __name__ == "__main__":
    # The name of the file our scraper created
    csv_file = 'python_jobs_with_descriptions.csv'
    analyze_job_skills(csv_file)