
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
    
    # output - empty list: 0
    if len(lst) == 0:
        return 0
    
    # output - non-empty list: sum of squares of odd numbers
    sums = 0
    for i in lst:
        if not (i % 2) and i > 0:
            sums += i * i
    return sums
    
    
    