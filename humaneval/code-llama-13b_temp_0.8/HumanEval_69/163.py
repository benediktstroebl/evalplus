
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
    # Your code here
    # Dict to save the frequency of the integers in lst
    freq = {}
    for elem in lst:
        freq[elem] = freq.get(elem,0) + 1
    
    # Find a candidate
    candidate = 1
    for key, value in freq.items():
        if key > candidate and key >= value:
            candidate = key

    # Check if candidate is a solution
    for key, value in freq.items():
        if key == candidate:
            if key < value:
                return -1
    
    return candidate
    
    
