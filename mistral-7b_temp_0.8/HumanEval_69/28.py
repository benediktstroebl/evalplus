
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
    if lst[0] > 1:
        return lst[0]
    count = {}
    for i in lst:
        count[i] = count.get(i,0) + 1
    maxCount = max(count.values())
    for key in count:
        if count[key] == maxCount and key > 1:
            return key
    return -1
