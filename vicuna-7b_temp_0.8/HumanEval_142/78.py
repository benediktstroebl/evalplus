


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
    # check if the list is empty
    if not lst:
        return 0
    
    # check if the last element of the list is a multiple of 3 or 4
    last_multiple = lst[-1] % 3 == 0 or lst[-1] % 4 == 0
    
    # create a new list to store the squared/cubed values
    squared_cubed = []
    
    # iterate over the list
    for num in lst:
        # if the last multiple is true, we cube the value
        if last_multiple:
            squared_cubed.append(num ** 3)
        # if the last multiple is false, we square the value
        else:
            squared_cubed.append(num ** 2)
    
    # add up the squared/cubed values and return the result
    result = sum(map(lambda x: x ** 2 if x % 3 == 0 else x ** 3 if x % 4 == 0 else x ** 2 if x % 3 == 0 else x ** 3, squared_cubed))
    
    return result

