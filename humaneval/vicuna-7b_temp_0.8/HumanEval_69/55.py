
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
    for i in range(len(lst)):
        freq = [0] * len(lst)
        for j in range(len(lst)):
            if j != i:
                freq[j] = lst[j] - lst[i]
        max_freq = max(freq)
        if max_freq >= len(lst):
            return max(freq)
    return -1

lst = [3, 1, 2, 1, 1, 1, 1, 1, 2, 3, 2, 3, 2, 1]
