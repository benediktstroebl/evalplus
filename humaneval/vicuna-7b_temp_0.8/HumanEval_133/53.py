

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
    # If the list is empty, return 0
    if not lst:
        return 0
    
    # Get the first number in the list
    first_num = lst[0]
    
    # Get the list with the first number removed
    remaining_lst = lst[1:]
    
    # Calculate the sum of squared numbers in the remaining list
    sum_of_squares = sum([x**2 for x in remaining_lst])
    
    # Return the result rounded to the upper int(Ceiling) first
    return round(sum_of_squares, 0)

lst = [5, 1, 2, 3, 4, 5]
