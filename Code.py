#Cloud Counselage Data Analtics Internship

#Intern Name: Sushant Aggarwal
#Intern ID: IP5437

'''We aim to conduct a comprehensive analysis to gain insights about 
relationship between their academic performance, event participation, career aspiration and factors influencing their success.

BASIC QUESTIONS (Attempt any 8)

1. How many uniqe students are included in the dataset?'''

import pandas as pd

#Reading the excel file
data = pd.read_excel('Data analyst Data.xlsx')

unique_students_count = data['Email ID'].nunique()
print("1. Number of unique students in the dataset:", unique_students_count)
print('''
      *****
''')

'''
2. What is the average GPA of the students?
'''

average_gpa = data['CGPA'].mean()
print("2. Average GPA of students:", average_gpa)
print('''
      *****
''')

'''
3. What is the distribution of students across different graduation years?
'''

distribution = data['Year of Graduation'].value_counts()
print("3. Distribution of students across different graduation years:")
print(distribution)
print('''
      *****
''')

'''
4. What is the distribution of student's experience with Python Programming?
'''

experience_distribution_in_python = data['Experience with python (Months)'].value_counts()
print("4. Distribution of students' experience with Python programming (Months):")
print(experience_distribution_in_python)
print('''
      *****
''')

'''
5. What is the average family income of the student?
'''

def income_range(income_range):
    if income_range == '7 Lakh+':
        return 7.5  
    elif income_range == '0-2 Lakh':
        return 1.0
    elif income_range == '5-7 Lakh':
        return 6.0
    elif income_range == '2-5 Lakh':
        return 3.5
    else:
        return None

# Preprocess family income
data['Family Income'] = data['Family Income'].apply(income_range)

# Calculate the average family income
average_income = data['Family Income'].mean()
print("5. Average family income of students:", average_income)

print('''
      *****
      ''')

'''
6. How does the GPA vary among different colleges? (Show top 5 results only)'''

# Calculating the average GPA for each unique college
college_gpa = data.groupby('College Name')['CGPA'].mean().sort_values(ascending=False)

# Display the top 5 results
print("6. Top 5 colleges based on average GPA:")
print(college_gpa.head(5))

print('''
      *****
      ''')

'''
7. Are there any outliers in the quantity(number if courses completed) attribute?'''

Q1 = data['Quantity'].quantile(0.25)
Q3 = data['Quantity'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(data['Quantity'] < lower_bound) | (data['Quantity'] > upper_bound)]
if len(outliers)>=1:

    print("7. Outliers in the 'Quantity' column:")
    print(outliers['Email ID'],outliers['Quantity'])
else:
  print("7. NO Outliers")
print('''
      *****
      ''')

'''
8. What is the average GPA for student from each city?'''

average_gpa_bycity = data.groupby('City')['CGPA'].mean()

print("8. Average GPA for students from each city:")
print(average_gpa_bycity)

print('''
      *****
      *****
      ''')

'''
MODERATE QUESTIONS (Attempt any 8)

10. How many students from various cities? (Using visualization tool)'''

import matplotlib.pyplot as plt
import numpy as np

city_counts = data['City'].value_counts()
top_cities = city_counts.head(10)

# Plotting the bar chart for top 10 cities
plt.figure(figsize=(10, 6))
top_cities.plot(kind='bar', color='skyblue')
plt.title('Top 10 Cities with Highest Number of Students')
plt.xlabel('City')
plt.ylabel('Number of Students')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plotting the grouped bar chart for all cities
plt.figure(figsize=(15, 8))
all_cities = city_counts[:20]  # Adjust this number based on the number of cities you want to display
all_cities.plot(kind='bar', color='skyblue')
plt.title('Number of Students from Various Cities')
plt.xlabel('City')
plt.ylabel('Number of Students')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


'''11. How does the expected salary vary based on factors like 'GPA', 'Family Income'
,'Experience with Python(Months)'?'''

import seaborn as sns
#Plot GPA vs Expected Salary
sns.scatterplot(data=data, x='CGPA', y='Expected salary (Lac)')
plt.title('GPA vs. Expected Salary')
plt.xlabel('CGPA')
plt.ylabel('Expected Salary (Lac)')
plt.show()

#Plot Family Income vs. Expected Salary
sns.scatterplot(data=data, x='Family Income', y='Expected salary (Lac)')
plt.title('Family Income vs. Expected Salary')
plt.xlabel('Family Income')
plt.ylabel('Expected Salary (Lac)')
plt.show()

#Plot with Experience with Python vs. Expected Salary
sns.scatterplot(data=data, x='Experience with python (Months)', y='Expected salary (Lac)')
plt.title('Experience with Python vs. Expected Salary')
plt.xlabel('Experience with Python (Months)')
plt.ylabel('Expected Salary (Lac)')
plt.show()

#Regression analysis
sns.lmplot(data=data, x='CGPA', y='Expected salary (Lac)')
plt.title('Linear Regression: GPA vs. Expected Salary')
plt.xlabel('CGPA')
plt.ylabel('Expected Salary (Lac)')
plt.show()

sns.lmplot(data=data, x='Family Income', y='Expected salary (Lac)')
plt.title('Linear Regression: Family Income vs. Expected Salary')
plt.xlabel('Family Income')
plt.ylabel('Expected Salary (Lac)')
plt.show()

sns.lmplot(data=data, x='Experience with python (Months)', y='Expected salary (Lac)')
plt.title('Linear Regression: Experience with Python vs. Expected Salary')
plt.xlabel('Experience with Python (Months)')
plt.ylabel('Expected Salary (Lac)')
plt.show()


'''12. Which event tend to attract more students from specific fields of study?'''

# Filter the data for students
student_data = data[data['Designation'] == 'Students']
# Count the occurrences of events for students
event_counts_for_students = student_data['Events'].value_counts()
# Find the event with the most occurrences for students
most_common_event_for_students = event_counts_for_students.idxmax()
print("12. Event that attract Most students:", most_common_event_for_students)
print('''
      
      *****
      ''')


'''13. Do students In leadership position during there college years tend to have higher GPAs or better expected salary?
'''
leadership_students = data[data['Leadership- skills'] == 'yes']
avg_gpa_leadership = leadership_students['CGPA'].mean()
avg_salary_leadership = leadership_students['Expected salary (Lac)'].mean()

# Calculate the average GPA and expected salary for students not in leadership positions
non_leadership_students = data[data['Leadership- skills'] == 'no']
avg_gpa_non_leadership = non_leadership_students['CGPA'].mean()
avg_salary_non_leadership = non_leadership_students['Expected salary (Lac)'].mean()

print("13. Average GPA of students in leadership positions:", avg_gpa_leadership)
print("Average expected salary of students in leadership positions:", avg_salary_leadership)
print("Average GPA of students not in leadership positions:", avg_gpa_non_leadership)
print("Average expected salary of students not in leadership positions:", avg_salary_non_leadership)
print('''
      
      *****
      ''')


'''14. How many students are graduating bt the end of 2024?'''

unique_students = data.drop_duplicates(subset='Email ID') #unique students based on their email

graduating_2024_unique = unique_students[unique_students['Year of Graduation'] <= 2024] #where year of graduation is by 2024

# Count the number of students graduating by the end of 2024
num_graduating_2024_unique = len(graduating_2024_unique)

print("14. Number of unique students graduating by the end of 2024:", num_graduating_2024_unique)
print('''
      
      *****
      ''')


'''15. Which promotion channel brings in more student participations for the event?'''

promotion_channel_counts = data.groupby('How did you come to know about this event?')['Quantity'].sum()
max_attendance_channel = promotion_channel_counts.idxmax()
max_attendance = promotion_channel_counts[max_attendance_channel]

print("15. Promotion channel with the highest attendance:", max_attendance_channel)
print("Number of attendees from this channel:", max_attendance)
print('''
      
      *****
      ''')

'''16. Find the total number of students who attended the events related to Data Science?'''

data_science_keywords = ['Data Science', 'Data Visualization', 'AI', 'ML','Artificial']
data_science_events = data[data['Events'].str.contains('|'.join(data_science_keywords), case=False)] ## Filter the dataset for events

total_attendees_data_science = data_science_events['Quantity'].sum()
print("16. Total number of students who attended Data Science events:", total_attendees_data_science)
print('''
      
      *****
      ''')

'''17. Those who have high CGPA and more experience in language those who had high expectations for salary? (Avg)'''

high_cgpa_threshold = 8.0  # Example threshold for high CGPA
high_experience_months = 6  # Example threshold for high experience in Python (months)

# Filter the dataset based on the criteria
filtered_data = data[(data['CGPA'] >= high_cgpa_threshold) & (data['Experience with python (Months)'] >= high_experience_months)]

# Calculate the average expected salary for the filtered students
average_salary_high_cgpa_high_experience = filtered_data['Expected salary (Lac)'].mean()
print("17. Average expected salary for students with high CGPA and more experience in Python:", average_salary_high_cgpa_high_experience,'in lacs')
