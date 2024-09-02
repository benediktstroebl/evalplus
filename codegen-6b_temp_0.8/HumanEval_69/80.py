
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
    # count = max_count = 0
    # for item in lst:
    #     if item > max_count:
    #         max_count = item
    #         count = 1
    #     elif item == max_count:
    #         count += 1
    # if count == 0:
    #     return -1
    # else:
    #     return max_count
    
    return next((x for x in lst if lst.count(x) >= x), -1)
