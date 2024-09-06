
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
    i = 0
    while i < n:
        if lst[i] > 0:
            max_val = max(lst[i], max_val)
            max_frequency = max(max_frequency, (lst[i] - 1) // (i + 1))
            i += 1
        elif i == n - 1:
            max_val = max_val + 1
            max_frequency = max_frequency + 1
        else:
            max_val = -1
    return max_val, max_frequency

n = int(input().strip())
lst = list(map(int, input().rstrip().split()))
max_val, max_frequency = search(lst)
