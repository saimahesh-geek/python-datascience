import pandas as pd

sal = pd.read_csv('Salaries.csv')

#head of dataset
#head = sal.head()

#num of entries
#sal.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 148654 entries, 0 to 148653
Data columns (total 13 columns):
Id                  148654 non-null int64
EmployeeName        148654 non-null object
JobTitle            148654 non-null object
BasePay             148045 non-null float64
OvertimePay         148650 non-null float64
OtherPay            148650 non-null float64
Benefits            112491 non-null float64
TotalPay            148654 non-null float64
TotalPayBenefits    148654 non-null float64
Year                148654 non-null int64
Notes               0 non-null float64
Agency              148654 non-null object
Status              0 non-null float64
dtypes: float64(8), int64(2), object(3)
memory usage: 14.7+ MB
"""

#Average BasePay
print('Avg BasePay : ')
print(sal['BasePay'].mean())

#Highest amount of OvertimePay
print('\nHighest OvertimePay : ')
print(sal['OvertimePay'].max())

#Job title of JOSEPH DRISCOLL
print('\nJob title of JOSEPH DRISCOLL : ')
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

#JOSEPH DRISCOLL total pay benifits
print('\nJOSEPH DRISCOLL total pay benifits : ')
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

#Higesht paid person including benifits
print('\nHighest paid person including benifits')
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'])

#print('\n ')
#print(sal.loc[sal['TotalPayBenefits'].idxmax()])
#print(sal.iloc[sal['TotalPayBenefits'].argmax()])

#Lowest paid person including benifits
print('\nLowest paid person including benifits')
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName'])

#Avg BasePay of all employees per year? (2011-2014)
print('\nAvg BasePay of all employees per year? (2011-2014)')
print(sal.groupby('Year').mean()['BasePay'])

#Number of unique job titles
print('\nNumber of unique job titles')
print(sal['JobTitle'].nunique())

#Top5 most common jobs
print('\nTop5 most common jobs')
print(sal['JobTitle'].value_counts().head(5))

#Number of job titles were represented by only one person in 2013 (i.e, job titile with only one occurrence in 2013)
print('\nJob titile with only one occurrence in 2013')
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))

#Number of people have the word Chief in their job title
def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False
    
print('\nNumber of people have the word Chief in their job title')
print(sum(sal['JobTitle'].apply(lambda x:chief_string(x))))

#Is there a correlation between length of the job Title string and salary?
sal['Title_len'] = sal['JobTitle'].apply(len)
print(sal[['Title_len', 'JobTitle']].corr())

#Note: https://www.kaggle.com/kaggle/sf-salaries (San Francisco city employee salary data)