
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
    # print(lst)
    # for i in lst:
    #     if lst.count(i) >= i:
    #         return i
    # return -1

    # if not lst:
    #     return -1
    # cur = lst[0]
    # for i in lst:
    #     if i > cur and lst.count(i) >= i:
    #         cur = i
    # return cur

    # if not lst:
    #     return -1
    # cur = lst[0]
    # for i in lst:
    #     if i > cur and lst.count(i) >= i:
    #         cur = i
    # return cur
    maxi = max(lst)
    max_count = lst.count(maxi)
    for i in lst:
        if lst.count(i) > max_count and i > 0:
            max_count = lst.count(i)
            maxi = i
    if max_count >= maxi:
        return maxi
    return -1

