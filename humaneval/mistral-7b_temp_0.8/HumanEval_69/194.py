
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
    # Solution
    max_freq = -1
    max_val = -1
    max_ind = 0
    for i in range(len(lst)):
        curr_val = lst[i]
        if curr_val > 0:
            freq = lst.count(curr_val)
            if freq >= curr_val:
                if freq > max_freq:
                    max_freq = freq
                    max_val = curr_val
                    max_ind = i
    return max_val if max_freq >= max_val else -1
    # Time: O(n)
    # Space: O(1)

