


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
    
    # Initialize accumulator
    summation = 0
    
    # Iterate over indices of the list
    for idx, value in enumerate(lst):
        
        # If index is a multiple of 3, square the value
        if idx % 3 == 0:
            summation += value**2
        
        # Else if index is a multiple of 4 but not 3, cube the value
        elif idx % 4 == 0:
            summation += value**3
        
        # Otherwise, keep the value
        else:
            summation += value
    
    # Return the sum of the accumulator
    return summation
