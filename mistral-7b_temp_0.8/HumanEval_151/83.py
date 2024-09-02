
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
    # set up the return value
    result = 0
    
    # loop through the list
    for x in lst:
        # if the value is odd and positive
        if x % 2 != 0 and x >= 0:
            # add it to the result
            result += x*x
    # return the result
    return result
