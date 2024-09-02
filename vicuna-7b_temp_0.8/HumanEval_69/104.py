
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
    max_frequency = 0
    max_index = 0
    for i, x in enumerate(lst):
        if x > 0 and x == lst[i]:
            max_frequency = max(max_frequency, i+1)
        elif x > 0:
            max_frequency = max(max_frequency, i+1)
            max_index = i
    return max_frequency, max_index

result = search([3, 3, 2, 3, 3])
