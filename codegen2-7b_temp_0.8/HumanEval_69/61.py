
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
    lst.sort()
    n = len(lst)
    if n == 1:
        return lst[0]
    if n == 2:
        return max(lst[1:])
    if lst[n-1] <= lst[0]:
        return lst[0]
    for i in range(n):
        if lst[i] >= lst[i+1]:
            return lst[i]
    return -
