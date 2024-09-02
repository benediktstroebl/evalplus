


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
    
    # check if the first element of the list is 0
    if lst[0] == 0:
        return 0
    
    # create a new list to store the squared and cubed values
    squared = []
    cubed = []
    
    # iterate through the list and check if the current element is a multiple of 3 or 4
    for i in range(len(lst)):
        # if the current element is a multiple of 3, square it
        if i % 3 == 0:
            squared.append(lst[i] ** 2)
            # if the current element is a multiple of 4, cube it
        elif i % 4 == 0:
            cubed.append(lst[i] ** 3)
        else:
            # otherwise, add the current element to the original list without modifying it
            lst.append(lst[i])
    
    # add all elements in the squared list to the original list
    lst += squared
    
    # add all elements in the cubed list to the original list
    lst += cubed
    
    # return the sum of all elements in the list
    return sum(lst)