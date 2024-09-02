
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

    #create a dictionary from the list
    frequencies = {}
    for i in lst:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1

    #iterate through dictionary and return the key with greatest frequency
    for key, value in frequencies.items():
        if value >= key:
            return key
    return -1
