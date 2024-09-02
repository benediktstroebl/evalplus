
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
    counter = {}
    res = 0
    for i in lst:
        counter[i] = counter[i] + 1 if i in counter else 1
        res = max(res, i)
    for i in range(res, -1, -1):
        if i in counter and i <= counter[i]:
            return i
    return -1
