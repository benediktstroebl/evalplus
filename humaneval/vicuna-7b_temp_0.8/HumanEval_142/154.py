


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
    
    # check if the list is empty
    if not lst:
        return 0
    
    # check if the number of entries in the list is a multiple of 3
    if len(lst) % 3 == 0:
        for i in range(len(lst)):
            if lst[i]**2 == lst[i]:
                lst[i] = lst[i]**2
        result = sum(lst)
        return result
    else:
        for i in range(len(lst)):
            if lst[i]**3 == lst[i]:
                lst[i] = lst[i]**3
            else:
                lst[i] = lst[i]**2
        result = sum(lst)
        return result
    
