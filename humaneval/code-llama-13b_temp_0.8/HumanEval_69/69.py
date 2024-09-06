
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
    # Solution 1
    # for item in set(lst):
    #     if lst.count(item) >= item:
    #         return item
    # return -1

    # Solution 2
    if len(lst) == len(set(lst)):
        return -1
    
    for item in lst:
        for i in range(item):
            if lst.count(i) == item:
                return item
    
    return -1

    # Solution 3
    # if len(lst) == len(set(lst)):
    #     return -1
    # l = sorted(lst)
    # for i in range(len(lst) - 1):
    #     for j in range(i + 1, len(lst)):
    #         if l[j] > l[i] and l.count(l[i]) >= l[i]:
    #             return l[i]

