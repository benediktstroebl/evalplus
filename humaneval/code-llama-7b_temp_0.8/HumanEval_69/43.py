
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
    freq = {}
    for i in lst:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    max_value = max(freq.keys())

    for k in freq:
        if k > max_value and freq[k] >= k:
            max_value = k
    if max_value >= max(freq.keys()):
        return max_value
    else:
        return -1

    # return max(freq.keys(), key=lambda x: (freq[x] >= x, -x)) or -1

