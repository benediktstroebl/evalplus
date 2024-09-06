
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
    
    # Use a dictionary to keep track of the squares of the odd numbers
    squares_dict = {}
    
    for num in lst:
        if num % 2 != 0 and not num % 1 == 0:
            # Get the square of the number
            square = num ** 2
            
            # If the square is not in the dictionary yet, add it
            if square not in squares_dict:
                squares_dict[square] = 0
                
            # Add the square to the dictionary
            squares_dict[square] += 1
    
    # The sum of squares of the odd numbers
    sum_of_squares = 0
    
    # Iterate over the dictionary and get the sum of squares
    for square, value in squares_dict.items():
        sum_of_squares += square * value
    
    return sum_of_squares
