

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    # A dictionary to keep track of squared numbers
    squared_numbers = {}
    
    # For each number
    for num in lst:
        # If the number is not in the dictionary
        if num not in squared_numbers:
            # Get the square of the number
            squared_num = num**2
            
            # Add the squared number to the dictionary
            squared_numbers[num] = squared_num
            
            # Add the square of the number to the total
            total += squared_num
    
    # Return the total
    return round(total, 0)