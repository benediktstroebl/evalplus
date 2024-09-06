
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
    # Set up a running total and square_count to track the sum and number of squares.
    total = 0
    square_count = 0
    # For each value in the list, check if it's odd and is greater than 0.
    for value in lst:
        # If the value is odd and greater than 0, add it to the total.
        if (value % 2 != 0) and (value > 0):
            total += value ** 2
            square_count += 1
    return total

