
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
    # 1. Create a dictionary where each key is a value and each value is the count of the value
    d = {}
    for val in lst:
        d[val] = d.get(val, 0) + 1
    # 2. Check each key to see if the value of the key is greater than the frequency of the key
    max_val = -1
    for val, freq in d.items():
        if val > freq:
            if max_val == -1:
                max_val = val
            else:
                max_val = max(max_val, val)
    return max_val if max_val != -1 else -1
