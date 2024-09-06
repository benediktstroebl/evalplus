
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
    
    # find the frequency of the numbers in the list
    freq = dict()
    for i in lst:
        freq[i] = freq.get(i, 0) + 1
    
    # check if there is a number whose frequency is equal to the number itself
    for i in lst:
        if i in freq and freq[i] >= i:
            return i
        
    return -1
