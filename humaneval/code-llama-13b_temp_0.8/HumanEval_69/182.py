
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
    hash_ = {}
    for i in lst:
        if i in hash_:
            hash_[i] += 1
        else:
            hash_[i] = 1
    res = []
    for k, v in hash_.items():
        if k > v:
            res.append(k)
    if len(res) > 0:
        return sorted(res)[-1]
    else:
        return -1

