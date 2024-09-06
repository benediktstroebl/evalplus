


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
    # use a for loop to go through each item in the list 
    # if the index is a multiple of 3, square the item
    # if the index is a multiple of 4, cube the item
    # if the index is not a multiple of 3 or 4, do nothing
    # return the sum of all items in the list 
    return_value = 0
    for i in range(0, len(lst)):
        if i % 3 == 0:
            return_value += lst[i] ** 2
        elif i % 4 == 0:
            return_value += lst[i] ** 3
        else:
            pass
    return return_value
