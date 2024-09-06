

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
    n = len(lst)
    # Check if the list is empty
    if n == 0:
        return 0
    
    # Initialize the result
    result = 0
    
    # Check for the last element
    if lst[-1] == 0:
        # Round the last element to the upper int(Ceiling)
        lst[-1] = round_to_ceiling(lst[-1])
        # Add the square of the last element to the result
        result += (lst[-1]**2)
        # Round the result to the upper int(Ceiling)
        result = round_to_ceiling(result)
    # For each element in the list
    for i in range(n-1, -1, -1):
        # Check if the element is positive
        if lst[i] >= 0:
            # Round the element to the upper int(Ceiling)
            lst[i] = round_to_ceiling(lst[i])
            # Add the square of the element to the result
            result += (lst[i]**2)
        else:
            # If the element is negative, switch the current
            # and next elements
            lst[i], lst[i+1] = lst[i+1], lst[i]
    
    return result
