


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
    if lst == []:
        return 0
    else:
        if lst[0] % 3 == 0 and lst[0] % 4 == 0:
            lst[0] = lst[0] ** 3
        elif lst[0] % 3 == 0:
            lst[0] = lst[0] ** 2
        if lst[1] % 4 == 0:
            lst[1] = lst[1] ** 3
        elif lst[1] % 3 == 0:
            lst[1] = lst[1] ** 2
        if lst[2] % 4 == 0 and lst[2] % 3 == 0:
            lst[2] = lst[2] ** 3
        elif lst[2] % 3 == 0:
            lst[2] = lst[2] ** 2
        return lst[0] + lst[1] + lst[2]

