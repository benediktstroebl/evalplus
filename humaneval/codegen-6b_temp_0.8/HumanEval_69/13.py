
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
    i = 0
    max_i = 0
    max_freq = 0
    while i < len(lst):
        if lst[i] > max_freq:
            max_freq = lst[i]
            max_i = i
        elif lst[i] == max_freq:
            max_i = max(max_i, i)
        i += 1
    return max_i if max_freq != 0 else -1

