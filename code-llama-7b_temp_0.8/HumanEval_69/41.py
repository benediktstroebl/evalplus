
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
    if lst.count(1) >= 1:
        return 1
    elif lst.count(2) >= 2:
        return 2
    elif lst.count(3) >= 3:
        return 3
    elif lst.count(4) >= 4:
        return 4
    elif lst.count(5) >= 5:
        return 5
    else:
        return -1


