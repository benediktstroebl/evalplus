
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
    n = len(lst)
    if n == 0:
        return -1
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            freq = 0
            for k in range(i, n):
                freq += lst[k]
            if lst[i] > freq and freq >= lst[i]:
                return lst[i]
    return -1

lst = [1, 2, 2, 3, 1]
result = search(lst)
