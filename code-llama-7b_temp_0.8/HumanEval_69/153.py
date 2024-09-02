
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
    # result = 0
    # for item in lst:
    #     if lst.count(item) >= item and item > 0:
    #         result = item
    # return result

    # dict_lst = {}
    # for item in lst:
    #     if item in dict_lst:
    #         dict_lst[item] += 1
    #     else:
    #         dict_lst[item] = 1

    # for key in dict_lst:
    #     if dict_lst[key] >= key:
    #         return key
    # return -1

    # result = -1
    # for key in lst:
    #     if key > 0:
    #         if lst.count(key) >= key and key > result:
    #             result = key
    # return result

    for key in lst:
        if key > 0 and lst.count(key) >= key:
            return key
    return -1


