
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
    # dictionary to keep frequency of each number
    d = dict()
    # iterate through the list
    for i in lst:
        # if number is 0, then it's greater than 0, and frequency is zero. 
        # So, we don't even need to check if number exists in dict.
        if i == 0:
            return -1
        # if the number exists in dict, then increment its frequency
        elif i in d:
            d[i] += 1
        # if number doesn't exist in dict, add it to dict with frequency 1
        else:
            d[i] = 1
    # iterate through the dictionary to check if the condition is satisfied
    for key in d:
        if d[key] >= key:
            return key
    return -1
    
    
