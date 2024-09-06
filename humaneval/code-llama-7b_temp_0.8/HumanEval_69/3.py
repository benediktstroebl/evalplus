
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # find the minimum value in the list
    # add 1 to the minimum value
    # create a dictionary
    # add the minimum value to the dictionary
    # add all other values to the dictionary
    # compare the dictionary to the original list
    # return the largest value that appears more than once

    # create a dictionary
    d = {}
    # find the minimum value in the list
    min_val = min(lst)
    # add 1 to the minimum value
    min_val = min_val + 1

    # create the dictionary
    for i in lst:
        # loop through the list
        if i == min_val:
            # if the item in the list is equal to the minimum value
            # add the item to the dictionary
            d[i] = d.get(i, 0) + 1
        else:
            # if the item in the list is not equal to the minimum value
            # add the item to the dictionary
            d[i] = d.get(i, 0) + 1
    # compare the dictionary to the original list
    for i in lst:
        # loop through the list
        if i == min_val:
            # if the item in the list is equal to the minimum value
            # return the largest value that appears more than once
            if d[i] >= i:
                return i
        else:
            # if the item in the list is not equal to the minimum value
            # return the largest value that appears more than once
            if d[i] >= i:
                return i
    # if no value is returned
    # return -1
    return -1

