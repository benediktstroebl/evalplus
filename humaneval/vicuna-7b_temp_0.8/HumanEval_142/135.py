


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
    # Check if the list is empty or not
    if not lst:
        return 0
    
    # Create a new list to store the result
    result = []
    
    # Loop through the list
    for i in range(len(lst)):
        # Check if the index is a multiple of 3
        if (i % 3 == 0):
            # If it is a multiple of 3, square it
            result.append(lst[i] * lst[i])
        # Check if the index is a multiple of 4
        elif (i % 4 == 0):
            # If it is a multiple of 4, cube it
            result.append(lst[i] * lst[i] * lst[i])
        # Otherwise, add the integer to the result list
        else:
            result.append(lst[i])
    
    # Return the sum of all entries in the result list
    return sum(result)