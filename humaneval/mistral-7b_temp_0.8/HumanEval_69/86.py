
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
    c = {}
    for item in lst:
        if item not in c:
            c[item] = 1
        else:
            c[item] += 1
    print(c)
    key_list = []
    for k, v in c.items():
        if v >= k:
            key_list.append(k)
    # print(key_list)
    max_key = max(key_list)
    # print(max_key)
    if max_key > 0:
        return max_key
    return -1

