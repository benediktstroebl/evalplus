
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
    # If the list is empty or not a list of integers, return 0
    if not lst or not isinstance(lst, list) or not all(map(int, lst)):
        return 0
    
    # Initialize a variable to store the sum
    sum = 0
    
    # Iterate through the list
    for num in lst:
        # If the number is odd
        if num % 2 != 0:
            # Add the square of the number to the sum
            sum += num ** 2
    
    return sum