
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

    # the list of items that match the criteria
    output = []
    
    # loop through the list of integers
    for num in lst:
        # if the number has a frequency greater than or equal to the number
        if lst.count(num) >= num:
            # add the number to the list
            output.append(num)
    
    # return the maximum number if the list has items
    if len(output) > 0:
        return max(output)
    # otherwise return -1
    else:
        return -1
