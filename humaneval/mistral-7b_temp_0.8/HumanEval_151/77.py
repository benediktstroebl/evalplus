
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    
    If the input list is empty, return 0.
    '''
    # 1. create a variable for the total sum of squared numbers
    # 2.
    # 3.
    # 4.
    # 5.
    # 6.
    # 7.
    # 8.
    # 9.
    # 10.
    # 11.
    # 12.
    # 13.
    # 14.
    # 15.
    # 16.
    # 17.
    # 18.
    # 19.
    # 20.

    # ignore negative or non-integer values
    lst = [i for i in lst if type(i) == int and i >= 0]

    # return 0 if lst is empty
    if len(lst) == 0:
        return 0

    # add the sum of the squared odd numbers
    return sum([i**2 for i in lst if i % 2 != 0])

