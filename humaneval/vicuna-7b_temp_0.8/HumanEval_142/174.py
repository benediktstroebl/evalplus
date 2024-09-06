


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
    # initialize sum to 0
    sum = 0
    
    # check if the list has at least 3 elements
    if len(lst) < 3:
        return sum
    
    # go through the list and square and cube every 3rd and 4th element respectively
    for i in range(len(lst)):
        # check if the index is a multiple of 3 or 4
        if (i % 3 == 0 or i % 4 == 0):
            # square or cube the element as appropriate
            if (i % 3 == 0):
                lst[i] = lst[i] ** 2
            else:
                lst[i] = lst[i] ** 3
        # add the element to the sum
        sum += lst[i]
    
    # return the sum
    return sum
