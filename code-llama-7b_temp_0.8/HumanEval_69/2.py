
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
    if len(lst) < 2:
        return -1
    if len(lst) == 2:
        if lst[1] >= lst[0]:
            return -1
        else:
            return lst[1]
    lst.sort()
    freq = {}
    for item in lst:
        if item not in freq:
            freq[item] = 1
        else:
            freq[item] += 1
    for item in freq:
        if freq[item] >= item:
            return item
    return -1
