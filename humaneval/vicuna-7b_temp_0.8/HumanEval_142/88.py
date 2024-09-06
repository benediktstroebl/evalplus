


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
    
    # check if the list has only one element
    if len(lst) == 1:
        return lst[0] ** 2 if lst[0] % 3 == 0 else lst[0] ** 3 if lst[0] % 4 == 0 else 0
    
    # get the list with odd indices
    odd_indices = [i for i in range(len(lst)) if i % 2 == 1]
    
    # iterate over the elements in the odd indices list
    for i in odd_indices:
        # calculate the square or cube of the element
        value = lst[i] ** 2 if lst[i] % 3 == 0 else lst[i] ** 3 if lst[i] % 4 == 0 else 0
        
        # add the value to the result
        result += value
    
    # return the result
    return result