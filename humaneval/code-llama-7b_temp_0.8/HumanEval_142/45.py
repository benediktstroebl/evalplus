


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
    # raise NotImplementedError
    
    #---Method 1-------------------------------------------------
    # lst1=[]
    # lst2=[]
    # lst3=[]
    # for i in range(len(lst)):
    #     if i%3==0:
    #         lst1.append(lst[i]**2)
    #     elif i%4==0 and i%3!=0:
    #         lst2.append(lst[i]**3)
    #     else:
    #         lst3.append(lst[i])
    # lst1=lst1+lst2+lst3
    # return sum(lst1)
    #------------------------------------------------------------

    #---Method 2-------------------------------------------------
    # lst1=[]
    # lst2=[]
    # lst3=[]
    # for i in range(len(lst)):
    #     if i%3==0:
    #         lst1.append(lst[i]**2)
    #     elif i%4==0 and i%3!=0:
    #         lst2.append(lst[i]**3)
    #     else:
    #         lst3.append(lst[i])
    # lst1=lst1+lst2+lst3
    # return sum(lst1)
    #------------------------------------------------------------

    #---Method 3-------------------------------------------------
    lst1 = [item ** 2 if i % 3 == 0 else item for i, item in enumerate(lst)]
    lst2 = [item ** 3 if i % 4 == 0 and i % 3 != 0 else item for i, item in enumerate(lst)]
    return sum(lst1 + lst2)
    #------------------------------------------------------------
