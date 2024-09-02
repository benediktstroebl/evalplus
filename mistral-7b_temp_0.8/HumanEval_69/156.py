
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
    freq_lst = [0 for i in range(len(lst))]
    for i in range(len(lst)):
        if lst[i] in freq_lst:
            freq_lst[lst[i] - 1] += 1
        else:
            freq_lst[lst[i] - 1] = 1
    for i in range(len(freq_lst) - 1, 0, -1):
        if freq_lst[i] >= i:
            return i
    return -1


