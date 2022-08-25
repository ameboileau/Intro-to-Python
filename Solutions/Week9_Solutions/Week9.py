# 
# Introduction to Python - Week 9 exercises
#

# import list
import enum
import numpy as np
import pandas as pd



# Exercise 1:
# Write a function that takes as input a list of 5 numbers and calculates the following quantities:
# the mean
# the median
# the sum
# the mode
# Hint: Use numpy!


def exercise_1(l):
    """
    Function that calculates the mean, median, sum, and mode of a list l
    l: list of numbers
    """

    mean = np.mean(l)
    med = np.median(l)
    s = np.sum(l)
    
    # The mode is a bit more difficult...
    # The mode is simply the value that repeats the most often in the list
    # If none of the values are repeated, it should return None
    # If multiple values are repeated the same number of times (e.g. [2, 2, 5, 5]), it should also return None

    uniques, repeat_cnts = np.unique(l, return_counts=True)  # Find the unique values, and their repetition counts

    # Find the maximum number of counts
    max_cnts = max(repeat_cnts)

    # Make sure it is unique
    if np.sum(repeat_cnts == max_cnts) == 1:

        # Access the most repeated value
        mode = uniques[repeat_cnts == max_cnts][0]
        
    else:
        mode = None

    return mean, med, s, mode




# Exercise 2:
# Write a function that takes as input two strings and combines them into one


def exercise_2(s1, s2):
    """
    Function that combines two strings together
    """

    return s1 + s2



# Exercise 3:
# Write a function that takes as input three lists and transforms them into a pandas DataFrame
# where the content of the lists make up the DataFrame columns


def exercise_3(l1, l2, l3):
    """
    Function that combines three lists into a pandas DataFrame, placing the list contents in the columns
    """

    df = pd.DataFrame(
        data = np.array([l1, l2, l3]).T  # Need to transpose the lists in order to switch them from row to column formation
    )

    return df



# ======================================================================================================



# Exercise 4:
# Write a function that takes as input a list of numbers and increases their value by their index


def exercise_4(l):
    """
    Function that takes as input a list of numbers and increases their value by their index
    l: list of numbers
    """

    new_l = []
    for i, c in enumerate(l):
        new_l.append(c + i)

    return new_l



# Exercise 5:
# Write a function that takes as input a list of numbers and calculates a list corresponding
# to the cumulative sum 
# e.g. input --> [0, 1, 2, 3, 4, 5]
# output --> [0, 1, 3, 6, 10, 15]


def exercise_5(l):
    """
    Function that calculates the cumulative sum of a list l
    l: list of numbers
    """

    new_l = []
    for i, c in enumerate(l):
        
        if i == 0:
            new_l.append(c)

        else:
            new_l.append(c + new_l[i-1])

    return new_l



# ======================================================================================================



# Exercise 6:
# Write a function that takes as input a variable v and tries to divide it by 2
# The code should print a meaningful message if it encounters an exception

def divide_by_two(v):
    """
    Function that divides a variable by two
    v: any object
    """

    try:
        return v/2
    except TypeError:
        print("Invalid object type for v:", type(v))




# Exercise 7:
# Write a function that takes as input a list and tries to calculate the sum
# The code should print a meaningful message if it encounters an exception
# Regardless of whether the code encounters an error, it should print out 'Code execution completed.'



def sum_of_list(l):
    """
    Function that calculates the sum of l
    l: any object type
    """

    try:
        return np.sum(l)
    except:
        print("An exception occured while l has object type:", type(l))
    finally:
        print("Code execution completed.")



# ------------------------------------------------------------------------------------------------------
#
# Run your code below!
#
# ------------------------------------------------------------------------------------------------------


print(exercise_1([1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 9, 10]))

print(exercise_2("Hello", "World"))

print(exercise_3(
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
))

print(exercise_4([1, 2, 3, 4, 5, 6]))

print(exercise_5([0, 1, 2, 3, 4, 5]))

print(divide_by_two("4"))

print(sum_of_list("hello world"))
