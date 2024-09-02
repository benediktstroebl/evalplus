


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
    # Create a new list and append all elements to it
    result = []
    for element in lst:
        # If the index is a multiple of 3, square the element
        if lst[i] % 3 == 0:
            result.append(lst[i] ** 2)
        # If the index is a multiple of 4, cube the element
        elif lst[i] % 4 == 0:
            result.append(lst[i] ** 3)
        # Append the element as is
        else:
            result.append(lst[i])
    # Concatenate the result list with the original list
    return sum(result)
