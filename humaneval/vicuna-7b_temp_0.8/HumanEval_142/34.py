


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
    # First, convert the list to a tuple
    lst = tuple(lst)
    
    # Check if the list has at least one entry
    if not lst:
        return 0
    
    # Initialize a variable to store the sum
    sum = 0
    
    # Iterate over the entries in the list
    for i in range(len(lst)):
        # Check if the index of the current entry is a multiple of 3
        if i % 3 == 0:
            # Square the current entry
            lst[i] = lst[i] ** 2
            sum += lst[i] ** 2
        # Check if the index of the current entry is a multiple of 4
        elif i % 4 == 0:
            # Cube the current entry
            lst[i] = lst[i] ** 3
            sum += lst[i] ** 3
        # Check if the index of the current entry is not a multiple of 3 or 4
        else:
            # Don't do anything to the current entry
    
    return sum