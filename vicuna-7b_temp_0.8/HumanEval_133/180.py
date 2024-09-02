

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
    # Find the maximum value
    max_val = max(lst)
    # Round the max value to the upper int(Ceiling)
    max_val = round(max_val)
    # Add the value to the square of itself
    total = (lst + [max_val**2])
    # Find the total of squared numbers
    total = [num**2 for num in total]
    # Round the total of squared numbers
    total = round(sum(total))
    return total
