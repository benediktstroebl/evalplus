
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
    count = [0] * len(lst)
    for num in lst:
        count[num] += 1
    max_num = max(count)
    max_freq = max_num if max_num > 0 else -1
    return max_freq

lst = [2, 1, 2, 3, 3, 1, 4, 1, 2]
