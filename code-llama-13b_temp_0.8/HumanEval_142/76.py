


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
    # Starting by assuming that the list is empty, then the sum will be 0
    sum_value = 0
    # For every value in the list, check if the index of the value is a multiple of 3. 
    for i in range(len(lst)):
        # if so, then the index of the value is a multiple of 3
        if i % 3 == 0:
            # then add the squared value to the sum value
            sum_value += lst[i] * lst[i]
    # For every value in the list, check if the index of the value is a multiple of 4.
    for i in range(len(lst)):
        # if so, then the index of the value is a multiple of 4
        if i % 4 == 0:
            # then add the cubed value to the sum value
            sum_value += lst[i] * lst[i] * lst[i]
    # return the sum value
    return sum_value
