


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    # Initialize a variable to hold the sum of the squared values
    sum_of_squares = 0
    
    # Iterate through the list
    for i, val in enumerate(lst):
        if (i % 3 == 0 and val % 3 != 0) or (i % 4 == 0 and val % 4 != 0):
            # If the value is squared or cubed, multiply it by its index
            multiplier = 1 if val % 3 == 0 and val % 4 == 0 else 3 if val % 4 == 0 else 4
            # Add the multiplied value to the sum_of_squares variable
            sum_of_squares += multiplier * val
    
    return sum_of_squares