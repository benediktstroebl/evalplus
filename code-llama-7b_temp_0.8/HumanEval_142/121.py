


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
    #set up an empty list to store the result
    result = []
    #for every entry in the input list
    for i in lst:
        #if the index is a multiple of 3:
        if i % 3 == 0:
            #square the entry
            result.append(i ** 2)
        #if the index is a multiple of 4, but not 3:
        elif i % 4 == 0:
            #cube the entry
            result.append(i ** 3)
        #otherwise, just leave the entry as is.
        else:
            result.append(i)
    #return the sum of all entries in the result list
    return sum(result)
