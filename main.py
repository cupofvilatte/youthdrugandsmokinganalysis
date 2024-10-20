# import pandas to use csv easily
import pandas as pd

# import tools to create graphs from the data
import matplotlib.pyplot as plt
import plotly.express as px

# save variable of file path for convenience
file_path = './youth_smoking_drug_data_10000_rows_expanded.csv'

# gender related to smoking study
def gender_smoking_study(csv_file):
    data = pd.read_csv(csv_file)

    gender_smoking_average = data.groupby('Gender')['Smoking_Prevalence'].mean()
    result = gender_smoking_average.idxmax() # identify gender with highest avg smoking
    
    ## Explanation of what the above code is essentially doing
    # # conditional statement to print whether men or women are dominant in the smoking industry
    # if gender_smoking_average['Male'] > gender_smoking_average['Female']:
    #     result = "Male"
    # elif gender_smoking_average['Female'] > gender_smoking_average['Male']:
    #     result = "Female"
    # else:
    #     result = "Equal"

    # print who is more likely as well as basic data about men and women related to smoking
    print(f"{result} is more likely to smoke.")
    print(gender_smoking_average)

# function to build a visualization of the gender/smoking function
def vizualize_gender_smoking(csv_file):
    data = pd.read_csv(csv_file)

    gender_smoking_average = data.groupby('Gender')['Smoking_Prevalence'].mean().reset_index()

    # create a bar chart
    # chat gpt helped understand syntax for these
    fig = px.bar(gender_smoking_average, x='Gender', y='Smoking_Prevalence',
                 title='Average Smoking Prevalence by Gender',
                 labels={'Smoking_Prevalence': 'Average Smoking Prevalence', 'Gender': 'Gender'})
    
    fig.show()

# question two of whether and how school activities are realted to trying drugs.
def school_activity_involement_study(csv_file):
    data = pd.read_csv(csv_file)

    # percent of those who are involved in school programs
    involved_avg = data[data['School_Programs'] == 'Yes']['Drug_Experimentation'].mean()

    # percent of those who are not involved in school programs
    not_involved_avg = data[data['School_Programs'] == 'No']['Drug_Experimentation'].mean()

    if not_involved_avg != 0:  # Avoid division by zero
        percent_difference = ((involved_avg - not_involved_avg) / not_involved_avg) * 100
    else:
        percent_difference = float('inf')

    # print results
    print(f"Average drug experimentation with school programs: {involved_avg:.2f}")
    print(f"Average drug experimentation without school programs: {not_involved_avg:.2f}")
    print(f"Percentage difference: {percent_difference:.2f}%")

# visualizial representation of the relationship between activies and drug use
def visualize_school_activity(csv_file):
    data = pd.read_csv(csv_file)

    involved_avg = data[data['School_Programs'] == 'Yes']['Drug_Experimentation'].mean()
    not_involved_avg = data[data['School_Programs'] == 'No']['Drug_Experimentation'].mean()

    # chat gpt helped for syntax
    fig = px.bar(x=['Involved', 'Not Involved'], y=[involved_avg, not_involved_avg],
                 title='Average Drug Experimentation Based on School Activity Involvement',
                 labels={'x': 'Involvement', 'y': 'Average Drug Experimentation'})
    
    fig.show()

def mental_health_correlation(csv_file):
    data = pd.read_csv(csv_file)

    mental_health_mapping = {
        'Poor': 1,
        'Fair': 2,
        'Good': 3,
        'Very Good': 4,
        'Excellent': 5,
        'Average': 6,
        'Above Average': 7,
        'Good to Very Good': 8,
        'Very Good to Excellent': 9,
        'Excellent to Exceptional': 10
    }

    data['Mental_Health_Numeric'] = data['Mental_Health']

    data['Drug_Experimentation'] = pd.to_numeric(data['Drug_Experimentation'], errors='coerce')

    data.dropna(subset=['Mental_Health_Numeric', 'Drug_Experimentation'], inplace=True)

    correlation = data['Mental_Health_Numeric'].corr(data['Drug_Experimentation'])

    
    print(f"Correlation between Mental Health and Drug Experimentation: {correlation:.2f}")

def visualize_mental_correlation(csv_file):
    data = pd.read_csv(csv_file)

    # Assuming Mental Health is already numeric from 1 to 10
    data['Mental_Health_Numeric'] = data['Mental_Health']  # If it's already numeric
    data['Drug_Experimentation'] = pd.to_numeric(data['Drug_Experimentation'], errors='coerce')

    # Drop NaN values
    data.dropna(subset=['Mental_Health_Numeric', 'Drug_Experimentation'], inplace=True)

    # Create scatter plot
    plt.scatter(data['Mental_Health_Numeric'], data['Drug_Experimentation'], alpha=0.5)
    plt.title('Mental Health vs. Drug Experimentation')
    plt.xlabel('Mental Health Score')
    plt.ylabel('Drug Experimentation Rate')
    plt.grid()
    plt.show()


# call gender study
gender_smoking_study(file_path)

print()
print("-" * 20)
print()

#call school activity study
school_activity_involement_study(file_path)

print()
print("-" * 20)
print()

mental_health_correlation(file_path)

vizualize_gender_smoking(file_path)
visualize_school_activity(file_path)
visualize_mental_correlation(file_path)