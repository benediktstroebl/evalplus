
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
    for i in lst:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    max_freq = max(freq_dict.values())
    if max_freq <= 1:
        return -1
    else:
        for i in freq_dict:
            if freq_dict[i] == max_freq:
                return i
        return -1
