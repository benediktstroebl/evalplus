


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
    # initialize a variable to hold the sum of squares
    s = 0
    
    # check if the length of the list is 0
    if len(lst) == 0:
        return 0
    
    # check if the length of the list is 1
    elif len(lst) == 1:
        # if the list has only one element, it must be the last element
        if lst[0] is lst[-1]:
            return lst[0] ** 2 + lst[0] ** 3
        else:
            return 0
    
    else:
        # iterate through the list
        for i in range(len(lst)):
            
            # check if the index is a multiple of 3
            if (i + 1) % 3 == 0:
                # check if the index is a multiple of 4
                if (i + 1) % 4 == 0:
                    # square the integer
                    s += lst[i] ** 2
                else:
                    # cube the integer
                    s += lst[i] ** 3
            else:
                # cube the integer
                s += lst[i] ** 3
    
    # return the sum of squares
    return s