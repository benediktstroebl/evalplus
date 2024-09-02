
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
    freq_dict = dict()
    for x in lst:
        if x in freq_dict:
            freq_dict[x] += 1
        else:
            freq_dict[x] = 1
    max_freq = -1
    for key in freq_dict:
        if freq_dict[key] > max_freq and key > 0:
            max_freq = freq_dict[key]
            max_key = key
    if max_freq == -1:
        return -1
    return max_key
