
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
    # Your code here
    # a = [4, 1, 2, 2, 3, 1]
    # b = [1, 2, 2, 3, 3, 3, 4, 4, 4]
    # c = [5, 5, 4, 4, 4]
    # d = [10, 5, 4, 4, 4]
    
    d = lst
    lst = list(set(lst))
    print(lst)
    # lst = [4, 1, 2, 3]
    # lst = [1, 2, 2, 3, 3, 3]
    # lst = [5, 4, 4, 4]
    # lst = [10, 5, 4, 4, 4]
    # lst = [10, 5, 4, 4, 1]
    print(lst)
    for i in lst:
        print(i)
        if i > 0 and i == lst.count(i):
            return i
    return -1

    # max_int = max(lst)
    # print(max_int)
    # freq = lst.count(max_int)
    # print(freq)
    # if freq >= max_int:
    #     return max_int
    # return -1

    # max_int = 0
    # freq = 0
    # for i in lst:
    #     if i > freq and i > max_int:
    #         freq = i
    #         max_int = i
    #     elif i > max_int:
    #         max_int = i
    #     if freq >= i and i > max_int:
    #         freq = i
    #     elif i > freq:
    #         freq = i
    #     print(i, freq, max_int)
    # return freq

    # max_int = 0
    # freq = 0
    # max_freq = 0
    # for i in lst
