

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
    # Check if the input is a list of numbers
    if not isinstance(lst, list) or not all(isinstance(x, int) for x in lst):
        return round(sum(map(round, lst)), 0)
    
    # Create an empty list to store the sum of squared numbers
    sum_of_squares = []
    
    # Iterate over the elements in the list
    for x in lst:
        # Calculate the squared value of the element
        squared_value = x**2
        
        # Add the squared value to the sum of squared numbers list
        sum_of_squares.append(squared_value)
        
    # Return the sum of squared numbers rounded to the upper int(Ceiling) first
    return round(sum(sum_of_squares), 0)
