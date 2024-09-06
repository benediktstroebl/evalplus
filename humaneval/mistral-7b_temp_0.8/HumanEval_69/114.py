
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
    # if lst == []:
    #     return -1
    # lst = list(set(lst))
    # max = max(lst)
    # max_count = 0
    # for i in lst:
    #     if lst.count(i) > i:
    #         max_count = lst.count(i)
    #     else:
    #         max_count = max
    # if max_count == 0:
    #     return -1
    # else:
    #     return max_count
    #
    #
    # # Below is another way to do this
    #
    # max = 0
    # max_count = 0
    # for i in lst:
    #     if lst.count(i) > i:
    #         max_count = lst.count(i)
    #     else:
    #         max_count = max
    # return max_count
    #
    # # or
    # max = max(lst)
    # max_count = lst.count(
