
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
    #if n==0 return -1
    if n==0:
        return -1
    freq = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            freq[i][j] = freq[j][i] + 1
    max_freq = 0
    for i in range(n):
        max_freq = max(max_freq, freq[i][i+1])
    max_val = n
    for i in range(n):
        max_val = max(max_val, i+freq[i][i+1])
    return max_val