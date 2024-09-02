
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
    # Check for empty list
    if not lst:
        return 0
    
    # Initialize result to 0
    result = 0
    
    # Check if the first number is odd or not an integer
    if not (lst[0] % 2 == 0 and int(lst[0]) >= 0):
        result = result + (lst[0]**2)
        
    # Check if the second number is odd or not an integer
    if not (lst[1] % 2 == 0 and int(lst[1]) >= 0):
        result = result + (lst[1]**2)
    
    # Check if the third number is odd or not an integer
    if not (lst[2] % 2 == 0 and int(lst[2]) >= 0):
        result = result + (lst[2]**2)
    
    # Check if the last number is odd or not an integer
    if not (lst[3] % 2 == 0 and int(lst[3]) >= 0):
        result = result + (lst[3]**2)
    
    return result
    
