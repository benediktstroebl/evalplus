


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
        new_lst = [lst[0]]
        for item in lst:
            if item!= new_lst[0]:
                new_lst.append(item)
    total = 0
    for item in new_lst:
        if (new_lst.index(item) % 3 == 0) and (new_lst.index(item) % 4!= 0):
            total += item**2
        elif (new_lst.index(item) % 3!= 0) and (new_lst.index(item) % 4 == 0):
            total += item**3
        else:
            total += item
    return total

