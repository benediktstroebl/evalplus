
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
    new_lst = lst[:]
    maximum = new_lst[0]
    maximum_freq = 1
    for idx, num in enumerate(lst):
        if num > 0 and num > maximum and num != maximum:
            maximum = num
            maximum_freq = 1
        elif num > 0 and num > maximum and num == maximum:
            maximum_freq += 1
            if maximum_freq > maximum:
                maximum = num
                maximum_freq = 1
    return maximum if maximum_freq >= maximum else -1

