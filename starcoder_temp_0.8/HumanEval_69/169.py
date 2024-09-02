
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
    hash_table = {}
    for item in lst:
        if item in hash_table.keys():
            hash_table[item] += 1
        else:
            hash_table[item] = 1
    
    max_key = max(hash_table, key=hash_table.get)
    if hash_table[max_key] >= max_key:
        return max_key
    else:
        return -1
