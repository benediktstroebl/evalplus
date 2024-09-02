
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
    # your code here
    # check if list is empty
    if not lst:
        return -1
    # find max
    max_value = max(lst)
    # check if max value is greater than 0
    if max_value > 0:
        # check if max value occurs more than once
        if lst.count(max_value) > 1:
            # return max value
            return max_value
        else:
            # check if max value occurs in list
            if max_value in lst:
                # return the next max value
                return search(lst[:-1])
            else:
                # return -1
                return -1
    else:
        # return -1
        return -1

