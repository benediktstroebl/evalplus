
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
    if len(lst) == 1:
        return -1
    lst.sort()
    lst_count = {}
    for i in range(len(lst)):
        if lst[i] in lst_count:
            lst_count[lst[i]] += 1
        else:
            lst_count[lst[i]] = 1
    res = -1
    for i in lst_count:
        if i == 0:
            continue
        elif lst_count[i] >= i:
            res = i
            break
    return res
