
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
    max_frequency = max(lst)
    max_index = 0
    for index in range(1, len(lst)):
        if lst[index] > 0 and lst[index] <= max_frequency:
            max_frequency = lst[index]
            max_index = index
    return max_index

lst = [4, 1, 2, 2, 3, 1]
result = search(lst)
