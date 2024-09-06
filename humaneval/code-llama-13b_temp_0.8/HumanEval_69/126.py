
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
    d = {}
    res = -1
    for el in lst:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    for key, value in d.items():
        if key > 0 and key >= value:
            if res < key:
                res = key
            else:
                res = res
        else:
            res = res
    return res
