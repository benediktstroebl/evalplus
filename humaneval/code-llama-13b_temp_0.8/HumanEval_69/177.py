
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
    if not lst:
        return -1

    highest_value = 0
    highest_frequency = 0
    for n in lst:
        if n > highest_value:
            highest_value = n
        if n == highest_value and n > highest_frequency:
            highest_frequency = n

    return highest_value if highest_frequency >= highest_value else -1
