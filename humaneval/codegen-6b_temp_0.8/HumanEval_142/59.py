


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
    
    lst_new = []
    summation = 0
    for i in range (0, len(lst)):
        p = 0
        if (i%3 == 0) & (i%4!=0):
            lst_new.append(lst[i]*lst[i])
            p = lst[i]*lst[i]
        elif (i%3!=0) & (i%4==0):
            lst_new.append(lst[i]**3)
            p = lst[i]**3
        else:
            lst_new.append(lst[i])
            p = lst[i]
        summation = summation + p
        
    return summation

