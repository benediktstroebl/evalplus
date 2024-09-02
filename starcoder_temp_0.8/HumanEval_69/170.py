
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
    hash_map = {}
    for i in lst:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1

    max_value = -1
    for key in hash_map:
        if key > max_value and hash_map[key] >= key:
            max_value = key
    return max_value if max_value > 0 else -1
