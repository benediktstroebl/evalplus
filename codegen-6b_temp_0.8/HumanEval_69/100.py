
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
    freq = {item: lst.count(item) for item in lst}
    maximum = None
    maximum_freq = None
    for num in freq:
        if freq[num] >= freq[maximum]:
            maximum_freq = freq[num]
            maximum = num
    return maximum if maximum_freq is not None else -1

from collections import Counter