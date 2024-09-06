
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
    if lst == []:
        return -1
    if len(lst) == 1:
        if lst[0] > 0:
            return lst[0]
        else:
            return -1
    if lst[0] == 0 or lst[0] == 1:
        if lst[0] == 0:
            return -1
        return search(lst[1:])
    if lst[1] < lst[0]:
        return -1
    for i in range(len(lst)):
        if lst[i] == 1:
            if lst[i+1] >= lst[i]:
                return search(lst[i+1:])
            else:
                return search(lst[i+2:])
        elif lst[i] > 1:
            if lst.count(lst[i]) >= lst[i]:
                return lst[i]
            else:
                return search(lst[i+1:])
    return -1

