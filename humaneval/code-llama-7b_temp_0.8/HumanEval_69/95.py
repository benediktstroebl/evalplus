
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
    for el in lst:
        if el not in freq.keys():
            freq[el] = 1
        else:
            freq[el] += 1
    freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[0], reverse=True)}
    for k in freq.keys():
        if freq[k] >= k:
            return k
    return -1

