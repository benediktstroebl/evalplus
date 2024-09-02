


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
    # Declare a variable and initialize it with zero
    result = 0
    # Go through each entry in the list
    for index, entry in enumerate(lst):
        # if index is multiple of 3, multiply the entry by itself
        if index % 3 == 0:
            entry *= entry
        # if index is multiple of 4 but not multiple of 3, cube the entry
        elif index % 4 == 0 and index % 3 != 0:
            entry **= 3
        # Add the entry to the result
        result += entry
    return result
