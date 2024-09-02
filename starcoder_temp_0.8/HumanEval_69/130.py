
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
    # set empty variable to hold max value
    max_int = 0
    # iterate through the list
    for num in lst:
        # if the value in the list is greater than zero
        if num > 0:
            # if the value in the list is greater than the max value
            if num > max_int:
                # set the value in the list to the max value
                max_int = num
    # return the max value
    return max_int
