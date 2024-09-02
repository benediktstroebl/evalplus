
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
    
    # check that the list is not empty and that each item is an integer
    if not lst:
        return 0
    
    try:
        for item in lst:
            if not item.isdigit():
                raise ValueError("List must include only integers")
    except AttributeError:
        raise ValueError("List must include only integers")
        
    sum_of_squares = 0
    
    for item in lst:
        if item % 2 == 1:
            sum_of_squares += (item**2)
    
    return sum_of_squares

