import pandas as pd

# Step 1: Load the data
df = pd.read_excel('jojoData.xlsx')

# Step 2: Drop unnecessary columns
df_cleaned = df.drop(columns=['Tijdstempel', 
                              'What features would make you more likely to use Zara’s digital clothing app? (Select all that apply)', 
                              'If you answered no in the question above, please express your opinion about the matter ', 'why do you buy new clothes ? '
                              , 'Would you be open to big companies like ZARA to start collecting second hand clothes from the brand ? ',
                              'Would you be open to buy second hand clothes from big companies like ZARA ? ',
                              'Do you believe fast fashion\'s companies should be more sustainable ? '])

# Step 3: Clean column names
df_cleaned.columns = df_cleaned.columns.str.strip()

# Step 4: Binary mapping for all remaining columns
binary_mapping = {
    'Male': 1, 'Female': 0, 
    'yes, sometimes': 1, 'no, never': 0, 'Yes, sometimes': 1, 'Yes, often': 1, 'No, never': 0, 
    'Yes, very often': 1, 'Not very interested': 0, 'Somewhat interested': 1, 
    'Very interested': 1, 'neutral': 0.5, 'Not interested at all': 0,
    'Yes': 1, 'No': 0
}
df_cleaned.replace(binary_mapping, inplace=True)

# Step 5: Handle Ordinal Data (mapping for age and other categories)
age_mapping = {'10-19': 1, '20-29': 2, '30-39': 3, '40-49': 4, '50+': 5}
df_cleaned['how old are you ?'] = df_cleaned['how old are you ?'].map(age_mapping)

clothes_freq_mapping = {
    'often - every month': 3,
    'Sometimes- every 2/3 months': 2,
    'Rarely - every 6 months or more': 1,
    'Once a year': 0,
}
df_cleaned['How often do you buy new clothes ( first hand clothes) ?'] = df_cleaned['How often do you buy new clothes ( first hand clothes) ?'].map(clothes_freq_mapping)

# Mapping for occupation status (are you?)
occupation_mapping = {'University student': 1, 'High school student': 0, 'Working full time': 2, 'Other': 3, 'None': 4}
df_cleaned['are you :'] = df_cleaned['are you :'].map(occupation_mapping)

# Step 5: Mapping for interest in recycling app
interest_mapping = {
    'Not interested at all': 0,
    'Not very interested': 1,
    'Neutral': 2,
    'Somewhat interested': 3,
    'Very interested': 4
}
df_cleaned['How interested would you be in using an app that rewards you with points for recycling used clothes, which can be redeemed for exclusive benefits like early access to new clothing lines?'] = df_cleaned['How interested would you be in using an app that rewards you with points for recycling used clothes, which can be redeemed for exclusive benefits like early access to new clothing lines?'].map(interest_mapping)

# Step 6: Handle missing data
df_cleaned.fillna(0, inplace=True)

# Step 7: Generate summary statistics
summary_stats = df_cleaned.describe(include='all')

# Step 8: Add variance, mode, mode frequency
summary_stats.loc['variance'] = df_cleaned.var(numeric_only=True)
mode = df_cleaned.mode().iloc[0]
summary_stats.loc['mode'] = mode
mode_freq = df_cleaned.apply(lambda x: x.value_counts().max())
summary_stats.loc['mode frequency'] = mode_freq

# Step 9: Covariance and Correlation matrix
covariance_matrix = df_cleaned.cov()

# Step 10: Display summary statistics, covariance and correlation matrices
print("Summary_stats:")
print(summary_stats)

print("Covariance Matrix:")
print(covariance_matrix)
