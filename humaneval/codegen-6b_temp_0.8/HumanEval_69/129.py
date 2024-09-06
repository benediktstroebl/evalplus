
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
    # 由于list里面的数都是正整数，因此最大的数肯定比它大的数都要大
    max_v = max(lst)
    max_index = lst.index(max_v)
    if max_v == 0:
        return -1
    else:
        return max(lst[:max_index] + lst[max_index+1:])

