
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
    freq = 0
    i = 0
    while i < len(lst):
        if lst[i] > 0:
            freq = lst[i]
            break
        i += 1

    if freq == 0:
        return -1

    lst = sorted(lst, reverse=True)
    count = 0
    i = 0
    while i < len(lst):
        if lst[i] == freq:
            count += 1
        else:
            if count >= freq:
                break
            count = 0
        i += 1

    if count >= freq:
        return lst[i - 1]
    else:
        return -1

