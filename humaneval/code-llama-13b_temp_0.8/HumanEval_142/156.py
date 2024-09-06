


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
    # NUMBER OF ENTRIES IN LIST
    count = 0
    for entry in lst:
        count = count + 1
    # COUNTS NUMBER OF ENTRIES THAT ARE MULTIPLES OF 3 AND 4
    count3 = 0
    for entry in lst:
        if entry % 3 == 0:
            count3 = count3 + 1
    count4 = 0
    for entry in lst:
        if entry % 4 == 0 and entry % 3 != 0:
            count4 = count4 + 1
    # IF LIST IS EMPTY, RETURN 0
    if count == 0:
        return 0
    # IF LIST IS NOT EMPTY, LOOP OVER ENTRIES AND MULTIPLY BY POWER OF 3 OR 4 IF INDEX IS MULTIPLE OF 3 OR 4
    else:
        for index in range(0,count-1):
            # IF INDEX IS MULTIPLE OF 3 AND NOT 4
            if lst[index] % 3 == 0 and lst[index] % 4 != 0:
                lst[index] = lst[index] * lst[index]
            # IF INDEX IS MULTIPLE OF 4 AND NOT 3
            elif lst[index] % 4 == 0 and lst[index] % 3 != 0:
                lst[index] = lst[index] * lst[index] * lst[index]
    # RETURN SUM OF ALL ENTRIES
    return sum(lst)
