
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
    # Solution 1
    # n = len(lst)
    # lst_dict = {}
    # for i in lst:
    #     if i not in lst_dict:
    #         lst_dict[i] = 1
    #     else:
    #         lst_dict[i] += 1
    # for i, j in lst_dict.items():
    #     if j >= i:
    #         return i

    # Solution 2
    n = len(lst)
    max_one = max(lst)
    if max_one < 0:
        return -1
    if n == 1:
        return max(lst)
    else:
        lst.remove(max_one)
        return max(lst)


