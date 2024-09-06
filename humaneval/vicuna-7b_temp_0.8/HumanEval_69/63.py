
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
    n = len(lst)
    max_value = 0
    max_frequency = 0
    for i in range(n):
        value = lst[i]
        frequency = lst.count(value)
        if value > max_value:
            max_value = value
            max_frequency = frequency
        if frequency >= value:
            break
    return max_value