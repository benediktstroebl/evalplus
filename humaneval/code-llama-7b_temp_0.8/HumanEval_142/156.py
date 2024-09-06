


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

    # Initialize variables
    index = 0
    summation = 0
    # Iterate over the list
    while index < len(lst):
        # Check if the current index is a multiple of 3
        if index % 3 == 0:
            # If it is a multiple of 3, square the entry
            summation += lst[index] ** 2
        else:
            # If it is not a multiple of 3, cube the entry
            summation += lst[index] ** 3
        # Increment the index
        index += 1
    # Return the sum of all entries
    return summation
