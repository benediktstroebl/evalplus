


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

    # Make a list to store the new values
    new_lst = []
    
    # Loop over the list and add the new values
    for idx, value in enumerate(lst):
        if (idx % 3 == 0) and (idx % 4 == 0):
            new_lst.append(value**3)
        elif (idx % 3 == 0):
            new_lst.append(value**2)
        elif (idx % 4 == 0):
            new_lst.append(value**3)
        else:
            new_lst.append(value)
    
    return sum(new_lst)

