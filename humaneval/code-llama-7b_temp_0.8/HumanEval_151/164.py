
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
    
    # list = [1, 3, 2, 0]
    
    # Set sum to 0
    total = 0
    
    # Iterate through list
    for value in lst:
        # Check if value is even and not negative
        if (value % 2) != 0 and value >= 0:
            # If value is even, square and sum
            total += value * value
            
    # Return sum
    return total
