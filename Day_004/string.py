# concatenating string
print('Thirty' + ' ' 'Days' + ' ' 'of' + ' ' 'python')
print('Coding' + ' ' 'For' + ' ' 'All')

# Declaring a variable
company = "Coding For All "
print(company)
company_length = len(company)
print( 'The length of the string {} is {}.'.format(company, company_length) )

# change lower case to upper case
print('lower case to upper case : ' ,company.upper())
# upper to lower
print('upper to lower : ' ,company.lower())
 
# capitalize()
print('first word capitalize : ' ,company.capitalize())
# title
print('Title case : ' ,company.title())
# swapcase()
print(company.swapcase())
# slicing first word out of Coding For All
company = "Coding For All "
first_word = company[0 : len('coding')]
print('fisrt word out of coding for all : ' ,first_word)



