
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
    l = []
    for i in lst:
        l.append((lst.count(i), i))
    r = sorted(l, key=lambda x: (x[0], -x[1]), reverse=True)
    for i in r:
        if i[0] >= i[1]:
            return i[1]
    return -1

