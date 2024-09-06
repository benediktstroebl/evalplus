
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
    # my solution
    if len(lst) == 0:
        return -1

    dict_freq = {}
    for i in lst:
        if i in dict_freq:
            dict_freq[i] += 1
        else:
            dict_freq[i] = 1

    max_num = 0
    max_num_freq = 0
    for key, value in dict_freq.items():
        if value > max_num_freq:
            max_num_freq = value
            max_num = key

    if max_num_freq < max_num:
        return -1
    else:
        return max_num

