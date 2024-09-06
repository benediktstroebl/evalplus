

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
    # Define a helper function to round the numbers
    def round_to_upper_int(x):
        return int(math.ceil(x))

    # Iterate through the list and sum the squares
    result = 0
    for num in lst:
        result += num ** 2
        
    # Round the result
    return round_to_upper_int(result)
