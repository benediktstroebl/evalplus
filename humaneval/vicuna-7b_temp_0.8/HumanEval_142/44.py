


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
    
    def handle_multiple_of_3(lst):
        newlst = []
        for i in range(len(lst)):
            if lst[i] % 3 == 0:
                newlst.append(lst[i]**2)
            else:
                newlst.append(lst[i])
        return newlst
    
    def handle_multiple_of_4(lst):
        newlst = []
        for i in range(len(lst)):
            if lst[i] % 4 == 0:
                newlst.append(lst[i]**3)
            else:
                newlst.append(lst[i])
        return newlst
    
    def handle_all_lst(lst):
        newlst1 = handle_multiple_of_3(lst)
        newlst2 = handle_multiple_of_4(lst)
        return newlst1+newlst2
    
    return handle_all_lst(lst)
