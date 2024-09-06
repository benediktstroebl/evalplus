
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
    
    # check for negative numbers or not integers
    for num in lst:
        if not (num >= 0 and num % 1 == 0):
            return 0
    
    # initialize sum to 0
    sum = 0
    
    # check for odd numbers and double the difference
    for num in lst:
        if num % 2 == 1:
            diff = num ** 2
            sum += diff
    
    return sum
