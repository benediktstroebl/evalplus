


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
    # test for empty list
    if not lst:
        return 0
    
    # define initial sum
    sum = 0
    
    # for each entry in the list
    for index, entry in enumerate(lst):
        # if the entry index is a multiple of 3
        if index % 3 == 0:
            # square the entry
            entry **= 2
        # if the entry index is a multiple of 4
        if index % 4 == 0:
            # and is not a multiple of 3
            if index % 3 != 0:
                # cube the entry
                entry **= 3
        # add the entry to the sum
        sum += entry
    
    return sum

