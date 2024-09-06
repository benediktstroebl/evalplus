
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
    # Keep a dictionary of the frequency of each number
    d = {}
    for i in lst:
        try:
            d[i] += 1
        except:
            d[i] = 1

    # Go through the dictionary, and find the number with the highest frequency
    max_freq = 0
    max_num = -1
    for num, freq in d.items():
        if freq > max_freq:
            max_freq = freq
            max_num = num

    return max_num
