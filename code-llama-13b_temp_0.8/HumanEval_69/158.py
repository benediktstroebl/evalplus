
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
    # if not lst:
    #     return -1
    # frequencies = {}
    # for i in lst:
    #     frequencies[i] = frequencies.get(i, 0) + 1
    # for i in range(max(lst), 0, -1):
    #     if frequencies.get(i, 0) >= i:
    #         return i
    # return -1

    # more concise version
    # return max(set(lst) - set(x for x in lst if x > 0 and lst.count(x) < x), default=-1)

    # more concise version with dictionary
    # from collections import defaultdict
    # dct = defaultdict(int)
    # for i in lst:
    #     dct[i] += 1
    # return max(x for x in set(lst) - set(k for k, v in dct.items() if v < k) if x > 0, default=-1)

    # cleanest way
    return max(
        set(lst) - 
        set(x for x in lst if x > 0 and lst.count(x) < x),
        default=-1)
