
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
    max_val = -1
    max_freq = -1
    for num in lst:
        if num > 0:
            freq = 1 + sum([1 for x in lst if x == num])
            if freq >= num:
                max_val = num
                max_freq = freq
    return max_val

lst = [1, 2, 2, 3, 1]
