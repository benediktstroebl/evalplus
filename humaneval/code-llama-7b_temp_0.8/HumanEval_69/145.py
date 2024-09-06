
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
    n = len(lst)
    max_freq = -1
    max_n = -1
    seen = dict()

    for i in range(n):
        x = lst[i]
        if x == 0:
            continue
        if x in seen:
            freq = seen[x] + 1
        else:
            freq = 1
        seen[x] = freq

        if freq >= x and x > max_n:
            max_freq = freq
            max_n = x

    if max_freq == -1:
        return -1
    else:
        return max_n
