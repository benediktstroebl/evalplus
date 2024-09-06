
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
    # Check if list is empty
    if len(lst) == 0:
        return 0
    # Check if list is all negative
    if len(lst) > 0 and all(x < 0 for x in lst):
        return 0
    # Check if list is all non-negative integers
    if len(lst) > 0 and all(x >= 0 and type(x) == int for x in lst):
        return sum(map(lambda x: x**2, filter(lambda x: x%2 != 0, lst)))
    return 0
