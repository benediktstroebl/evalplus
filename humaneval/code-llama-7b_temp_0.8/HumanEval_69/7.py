
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
    # my solution
    # return -1
    # if not lst:
    #     return -1
    # for num in lst:
    #     if lst.count(num) >= num:
    #         return num
    # return -1

    # guided answer
    result = -1
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1] and lst[i] > 0 and lst.count(lst[i]) >= lst[i]:
            result = lst[i]
    return result
    
    # another solution
    # from collections import Counter
    # def search(lst):
    #     if not lst:
    #         return -1
    #     counter = Counter(lst)
    #     for i in range(1, len(lst)):
    #         if counter[lst[i]] >= lst[i] and lst[i] > lst[i - 1]:
    #             return lst[i]
    #     return -1



