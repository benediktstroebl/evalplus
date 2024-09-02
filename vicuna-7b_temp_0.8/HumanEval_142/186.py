


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
    # Create an empty list to store the squared and cubed values
    squared_cubed = []
    for x in lst:
        if x % 3 == 0:
            squared_cubed.append(x**2)
        elif x % 4 == 0:
            squared_cubed.append(x**3)
        else:
            squared_cubed.append(x)
    
    # Add the squared and cubed values
    squared_cubed = sum(squared_cubed)
    # Add the remaining values
    sum_of_rest = sum(lst)
    
    # Return the sum of squared and cubed values
    return sum_of_rest + squared_cubed
