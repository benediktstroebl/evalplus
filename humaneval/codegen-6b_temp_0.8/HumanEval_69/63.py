
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
    seen = {}
    # frequency = 0
    maximum = -1
    # for i in range(len(lst)):
    #     if lst[i] in seen:
    #         frequency = frequency + 1
    #         if (maximum < frequency):
    #             maximum = frequency
    #     else:
    #         frequency = 0
    # return maximum
    maximum = -1
    for i in range(len(lst)):
        frequency = 0
        if lst[i] in seen:
            frequency = seen[lst[i]] + 1
            if (maximum < frequency):
                maximum = frequency
        else:
            frequency = 0
        seen[lst[i]] = frequency
    return maximum

