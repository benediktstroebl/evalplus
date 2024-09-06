
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
    # Write your code here
    if not lst:
        return -1
    # dict: key = int, value = num of times
    dic = {}
    max_num = max(lst)
    max_value = 0
    for x in lst:
        if x in dic.keys():
            dic[x] += 1
        else:
            dic[x] = 1
    # if the value of the key is not in the key, then the value is 0
    for key, value in dic.items():
        if value >= key and key > 0:
            if value > max_value:
                max_value = value
                max_num = key
    if max_value == 0:
        return -1
    return max_num
