
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
    # solution 1
    # nums = {n:lst.count(n) for n in lst}
    # sorted_nums = sorted(nums.items(), key=lambda x: x[1])
    # if sorted_nums[-1][0] <= 0:
    #     return -1
    # return sorted_nums[-1][0]

    # solution 2
    # max_n = -1
    # for n in lst:
    #     if max_n < n and lst.count(n) >= n:
    #         max_n = n
    # return max_n

    # solution 3
    d = {}
    for i in lst:
        d[i] = d.get(i,0) + 1
    for i in sorted(d, reverse=True):
        if d[i] >= i:
            return i
    return -1
