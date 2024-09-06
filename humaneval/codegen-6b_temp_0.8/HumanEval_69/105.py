
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
    def calc_freq(li):
        freq = {}
        for item in li:
            if not freq.get(item):
                freq[item] = 0
            freq[item] += 1
        return freq
    
    if len(lst) == 0:
        return -1
    
    freq = calc_freq(lst)
    max_len = len(str(max(lst)))
    candidates = []
    for val, freq in freq.items():
        candidates.append((val, freq, max_len - len(str(val))))
    return max(candidates, key=lambda x: x[1]*x[2])[0]
