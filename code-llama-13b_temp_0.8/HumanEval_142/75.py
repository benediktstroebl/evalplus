


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

    # 1- l = list()
    # 2- loop for each entry in lst
    # 3- if i%3 == 0:
    # 4-  l.append(i*i)
    # 5- else if i%4 == 0:
    # 6-  l.append(i*i*i)
    # 7- else:
    # 8-  l.append(i)
    # 9-  sum(l)

    l= list()
    for i in lst:
        if i%3 ==0:
            l.append(i**2)
        elif i%4 ==0:
            l.append(i**3)
        else:
            l.append(i)
    return sum(l)







