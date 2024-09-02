


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
    
    # initialize a variable to store the sum of the squares
    sum = 0
    
    # check if the first element is a multiple of 3
    is_multiple_3 = (lst[0] % 3) == 0
    
    # check if the last element is a multiple of 4
    is_multiple_4 = (lst[-1] % 4) == 0
    
    # if the first element is a multiple of 3, square the first element. If the last element is a multiple of 4, cube the last element
    if is_multiple_3:
        sum += lst[0] ** 2
    elif is_multiple_4:
        sum += lst[-1] ** 3
    
    # if the first element is not a multiple of 3, move to the second element
    for i in range(1, len(lst)):
        is_multiple_3 = (lst[i] % 3) == 0
        if is_multiple_3:
            sum += lst[i] ** 2
        else:
            # if the current element is not a multiple of 3, move to the next element
            break
    
    # if the last element is not a multiple of 4, move to the second to last element
    for i in range(len(lst)-1):
        is_multiple_4 = (lst[i] % 4) == 0
        if is_multiple_4:
            sum += lst[i+1] ** 3
        else:
            # if the current element is not a multiple of 4, move to the next element
            break
    
    return sum

