


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
    # check if index is a multiple of 3 or 4
    # if so, square the entry
    # if not, cube the entry
    # do not change the entry
    return lst[0] + (lst[1]**2 if ((lst[0] % 3 == 0) or (lst[0] % 4 == 0)) else (lst[1]**3 if not (lst[0] % 3 == 0) else lst[1]**2)) + \
        3*lst[2]*(lst[2]**2 if ((lst[1] % 3 == 0) and (lst[0] % 4 == 0)) else (lst[2]**3 if not (lst[1] % 3 == 0) else lst[2]**2)) + \
        3*(lst[0] if (lst[0] % 3 == 0) else 0) + \
        3*(lst[3] if (lst[1] % 3 == 0) else 0)
