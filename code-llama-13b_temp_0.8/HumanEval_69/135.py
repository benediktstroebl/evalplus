
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
    # return 1
    # list_set = set(lst)
    # for item in list_set:
    #     if item < len(lst):
    #         if lst.count(item) >= item:
    #             return item
    # return -1

    # dict = {}
    # for item in lst:
    #     if item in dict:
    #         dict[item] += 1
    #     else:
    #         dict[item] = 1
    # print(dict)
    # max_freq = 0
    # max_item = -1
    # for k,v in dict.items():
    #     if v > max_freq:
    #         max_item = k
    #         max_freq = v
    # return max_item

    # return max([item for item in lst if lst.count(item) >= item])
    # return max((item for item in lst if lst.count(item) >= item), default=-1)
    # return max(item for item in lst if lst.count(item) >= item) if [item for item in lst if lst.count(item) >= item] else -1
    # return max([item for item in lst if lst.count(item) >= item]) or -1

    lst_set = set(lst)
    for item in lst_set:
        if item <= 0:
            continue
        if lst.count(item) >= item:
            return item
    return -1


