
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
    # Create a new list that contains the frequency of each integer in the original list
    freqs = [lst.count(i) for i in lst]
    # Find the maximum frequency of an integer in the list
    max_freq = max(freqs)
    # Find the greatest integer that has a frequency greater than or equal to its value
    for i in range(max_freq, max(freqs) + 1):
        if freqs[i] >= i:
            return i
    return -1
