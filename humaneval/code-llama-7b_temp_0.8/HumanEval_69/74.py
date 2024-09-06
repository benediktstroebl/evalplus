
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
    # put all the numbers in a dictionary where the key is the number and the value is the number of occurrences
    d = {}
    for i in lst:
        d[i] = d.get(i,0) + 1

    # find the numbers with frequencies greater than or equal to the number itself
    freq = {}
    for k in d:
        if d[k] >= k:
            freq[k] = d[k]
    # if there are any such numbers then return the number with the largest value
    if freq:
        return max(freq)
    # otherwise return -1
    else:
        return -1


