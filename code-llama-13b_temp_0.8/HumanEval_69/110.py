
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
    
    # freq stores the frequency of each unique element in the list
    freq = {}
    # max_freq will store the frequency of the element with the greatest frequency
    max_freq = 0
    # el stores the element with the greatest frequency
    el = None
    for x in lst:
        if x not in freq:
            freq[x] = 0
        freq[x] += 1
        if freq[x] >= x and freq[x] > max_freq:
            el = x
            max_freq = freq[x]
    return el

