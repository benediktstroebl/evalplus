

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
    # Lets start with sum of squares, which is the sum of the square of each element of the list
    sum_squares = 0
    # Lets start with the sum, which is the sum of each element of the list
    sum = 0
    # For each element in the list
    for el in lst:
        # Round the element to the ceiling first
        rounded = math.ceil(el)
        # Sum of squares the squared value of the rounded value
        sum_squares += rounded**2
        # Sum the value of the rounded value
        sum += rounded
    
    # Return the difference of sum and sum of squares, since we want sum of squares, not sum of squares minus sum
    return sum_squares - sum
