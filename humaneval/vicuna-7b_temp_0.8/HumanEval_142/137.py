


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
    # Check if list is empty
    if not lst:
        return 0
    
    # Initialize counter to track number of cubed entries
    counter = 0
    
    # Iterate through each element in the list
    for i, val in enumerate(lst):
        # Check if index is a multiple of 3
        if (i % 3 == 0):
            # If so, square the value
            lst[i] = val**2
            counter += 1
        elif (i % 4 == 0):
            # If not, cube the value
            lst[i] = val**3
            counter += 1
        else:
            # If index is not a multiple of 3 or 4, do not change the value
            pass
    
    # Add all entries to calculate sum
    return sum(lst)
