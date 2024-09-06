
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
    freq = {x: 0 for x in lst}
    max_val = max(lst)
    max_freq = 0
    for i in range(len(lst)):
        if lst[i] > max_val - 1:
            max_val = lst[i]
            max_freq = freq[lst[i]]
    return max_freq