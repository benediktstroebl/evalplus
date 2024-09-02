
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
    dic = {}
    for i in lst:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    keys = list(dic.keys())
    for i in range(len(keys)):
        if keys[i] >= dic[keys[i]] and (i == len(keys)-1 or dic[keys[i]] > dic[keys[i+1]]):
            return keys[i]
    return -1
