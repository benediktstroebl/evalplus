
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

    freq_dict = {}

    for i in lst:
        if i in freq_dict.keys():
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1

    max_val = -1

    for i in lst:
        if i > 0 and freq_dict[i] >= i:
            if i > max_val:
                max_val = i

    if max_val > 0:
        return max_val
    else:
        return -1



