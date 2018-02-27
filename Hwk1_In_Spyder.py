import numpy as np

# This value-checking code was repeated 4 times, so I put it in a function.
# It compares value to check_value, and prints a single value if they match
# or both values if they don't.
def compare(name, value, check_name, check_value):
    if value == check_value:
        print('The', name, 'matches', check_name, 'and is', value)
    else:
        print('The', name, 'is', value)
        print('It is not exactly the same as', check_name, 'which is ', check_variance)
    return

# Question 1 (similar to class):
# An oceanographer is studying wintertime sea surface temperature at a site on
# the east coast. For the past six years, she obtains the following values:
#
# [8.61, 7.575, 9.72, 2.087, 5.421, 1.659]
#
# In the space below, write a program that
# calculates the mean, and prints it on the screen. Use the built-in sum() and
# len() functions. Avoid using np.mean(), except to check your work. Use
# descriptive variable names -- see Section 2.12 of Python for Everybody.

values = np.array([8.61, 7.575, 9.72, 2.087, 5.421, 1.6594])
total = sum(values)
count = len(values)
mean_value = total/count
check_mean = np.mean(values)
print('Q1:')
compare('mean', mean_value, 'np.mean', check_mean)

# Question 2:
# Write a program the calculates and prints the (unbiased) variance of the same
# SST data set and prints it to the screen. Re-use variables that you created
# in your answer to Question 1.  Avoid using np.var(), except to check your
# work. Note that the "ddof" option in np.var() needs to be modified to compute
# the unbiased variance.
deltas = values - mean_value
variance = sum(deltas**2)/(count-1)
check_variance = np.var(values, ddof=1)
print('Q2:')
compare('variance', variance, 'np.var with N-1 degrees of freedom', check_variance)


# Question 3:
# Write a program the calculates and prints the standard deviation of the same
# SST data set and prints it to the screen. Avoid using np.std(), except to check
# your work.
stdev = variance**0.5
check_stdev = np.std(values, ddof=1)
print('Q3:')
compare('standard deviation', stdev, 'np.std', check_stdev)

# Question 4:
# Write a program the calculates and prints the standard error of the same
# SST data set and prints it to the screen.
std_error = stdev/count**0.5
from scipy import stats
check_std_error = stats.sem(values, ddof=1)
print('Q4:')
compare('standard error', std_error, 'stats.sem', check_std_error)

# Question 5:
# Write a program that prints the z-scores of the same SST data set.
z_score = (values - mean_value) / stdev
print('Q5:')
print('For values    ', np.round(values, 3))
print('the z-score is', np.round(z_score, 3))



# Question 6:
# Write a program that takes the last value from SST data set created in
# Question 1, and rounds it to the nearest tenth. Hint: help(round)
# Make sure that all of your programs in questions 1-6 still work if
# new value is added to the end of the data set.
print('Q6:')
print('\nLast SST value, rounded to tenths: ', round(values[-1], 1))



# Question 7:
# (Excercise 5 in Chapter 2 of Python for Everybody)
# Write a program which prompts the user for a Celsius temperature, convert the
# temperature to Fahrenheit, and print out the converted temperature.
print('Q7:')
cel = input('Enter a Celsius temperature:')
try:
    cel_value = float(cel)
    fahrenheit = (cel_value*1.8) + 32
    print(cel, 'Celsius is ',fahrenheit, 'Fahrenheit')
except:
    print('I only understand numbers.  Please come back later.')
        

# Question 8:
# Write a program that uses input to prompt a user for their first and last names
# and then welcomes them using their initials. For example:
#
# Enter your first name: Tom
# Enter your last name: Connolly
# Hello TC!
print('Q8:')
first = input('Enter your first name:')
last = input('Enter your last name:')
if len(first):
    first_i = first[0]
else:
    first_i = ''
if len(last):
    last_i = last[0]
else:
    last_i = ''    
print('Hello', first_i + last_i)

