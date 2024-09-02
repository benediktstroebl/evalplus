
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
    max_val, max_frequency, max_index = 0, 0, 0
    for num in lst:
        count = lst.count(num)
        if count >= num:
            max_val = max(max_val, num)
            max_frequency = max(max_frequency, count)
            max_index = max(max_index, i)
    return max_val, max_frequency, max_index

lst = [2, 1, 2, 2, 3, 1, 4, 4, 4]
