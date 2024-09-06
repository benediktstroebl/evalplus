
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
    # check for empty list
    if not lst:
        return 0
    
    # check for negative numbers or non-integers
    for num in lst:
        if num < 0 or not num % 1 == 0:
            return 0
    
    # get list of odd numbers
    odd_nums = [x for x in lst if x % 2 != 0]
    
    # get sum of squares of odd numbers
    squared_odd_nums = [x**2 for x in odd_nums]
    sum_of_squares = sum(squared_odd_nums)
    
    # return sum of squares
    return sum_of_squares
