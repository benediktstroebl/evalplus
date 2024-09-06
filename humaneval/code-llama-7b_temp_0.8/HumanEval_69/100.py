
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
    if len(lst) == 1 and lst[0] == 1:
        return -1
    else:
        freq = {}
        for num in lst:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
    max_freq = max(freq.items(), key=lambda x: x[1])
    max_freq_num, max_freq_val = max_freq
    if max_freq_val >= max_freq_num:
        return max_freq_num
    else:
        return -1
