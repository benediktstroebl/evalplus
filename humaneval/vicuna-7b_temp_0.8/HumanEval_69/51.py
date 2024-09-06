
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
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    max_val = max(freq.values())
    max_val_idx = freq[max_val]
    
    for val in freq.keys():
        if freq[val] >= val:
            freq[val] -= val
            max_val_idx = max(max_val_idx, val + 1)
    
    return max_val_idx

lst = [1, 2, 2, 3, 1]
