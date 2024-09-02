
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
    # 1. Use a dictionary to keep track of the frequency of all elements in the array
    # 2. Using the dictionary, iterate over the list
    # 3. Find the element whose frequency is greater than the number itself
    # 4. Return the first such element
    # 5. If no such element is found, return -1
    
    frequencies = {}
    for n in lst:
        if n not in frequencies:
            frequencies[n] = 1
        else:
            frequencies[n] += 1
    
    for n in lst:
        if frequencies[n] >= n:
            return n
    
    return -1
