
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
    max_key = max(lst)
    for num in lst:
        if num > 0:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
    for i in range(1, max_key + 1):
        if i in dic and i <= dic[i]:
            return i
    return -1
