import pandas as pd

ecom = pd.read_csv('Ecommerce Purchases')

#info = ecom.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10000 entries, 0 to 9999
Data columns (total 14 columns):
Address             10000 non-null object
Lot                 10000 non-null object
AM or PM            10000 non-null object
Browser Info        10000 non-null object
Company             10000 non-null object
Credit Card         10000 non-null int64
CC Exp Date         10000 non-null object
CC Security Code    10000 non-null int64
CC Provider         10000 non-null object
Email               10000 non-null object
Job                 10000 non-null object
IP Address          10000 non-null object
Language            10000 non-null object
Purchase Price      10000 non-null float64
dtypes: float64(1), int64(2), object(11)
memory usage: 1.1+ MB
"""

#head = ecom.head()

print('Columns list')
print(ecom.columns)

print('\nNumber of rows')
print(len(ecom.index))

print('\nAverage purchase price')
print(ecom['Purchase Price'].mean())

print('\nHighest purchase price')
print(ecom['Purchase Price'].max())

print('\nLowest purchase price')
print(ecom['Purchase Price'].min())

print('\nNumber of people with English en as their language of choice on the website')
print(ecom[ecom['Language'] == 'en']['Language'].count())

print('\nNumber of people with job title as Lawyer')
print(ecom[ecom['Job'] == 'Lawyer']['Job'].count())

print('\nNumber of people made the purchase during the AM or PM')
print(ecom['AM or PM'].value_counts())

print('\nTop 5 most common job titles')
print(ecom['Job'].value_counts().head())

print('\nPurchase price for the transaction came from Lot: 90WT')
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])

print('\nNumber of people with American Express as their Credit Card and made a purchase above 95$')
print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price']>95)]['CC Provider'].count())

print('\nNumber of people have a credit card that expires in 2025')
print(ecom[ecom['CC Exp Date'].apply(lambda x:x[:2] == 25)]['CC Exp Date'].count())

print('\nTop 5 email providers')
print(ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head())

