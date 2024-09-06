


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
    # check that the input is a list
    if not isinstance(lst, list):
        return None
    
    # create an empty list to add results to
    result = []
    
    for idx, val in enumerate(lst):
        # check if the current index is a multiple of 3 or 4
        if idx % 3 == 0:
            # if the index is a multiple of 3, square the value and add to the result
            result.append(val**2)
        elif idx % 4 == 0:
            # if the index is a multiple of 4, cube the value and add to the result
            result.append(val**3)
        else:
            # if the index is not a multiple of 3 or 4, add the value to the result
            result.append(val)
            
    # add all the values in the result to get the total and return it
    return sum(result)

