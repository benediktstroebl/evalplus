


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
    elif len(lst) == 1:
        if lst[0] % 3 == 0:
            return lst[0] ** 2
        elif lst[0] % 4 == 0:
            return lst[0] ** 3
    else:
        sum1 = 0
        sum2 = 0
        for i in range(len(lst)):
            if i % 3 == 0:
                sum1 += lst[i] ** 2
            elif i % 4 == 0:
                sum2 += lst[i] ** 3
        return sum1 + sum2

