
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
    
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    # most_freq = None
    # most_freq_val = None
    # for i in dic:
    #     if most_freq is None or dic[i] >= most_freq_val:
    #         most_freq = i
    #         most_freq_val = dic[i]
    # return most_freq if most_freq is not None else -1
    
    #second solution
    for k in dic:
        if dic[k] >= k:
            return k
    return -1
