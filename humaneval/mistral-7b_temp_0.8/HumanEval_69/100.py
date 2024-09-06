
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
    lst.sort()
    if len(lst) == 1:
        return -1
    a = 1
    while lst[a] == lst[a-1]:
        a += 1
    print(a)
    b = lst[a]
    while b < len(lst):
        if lst[b] == lst[b-1]:
            b += 1
        else:
            break
    print(b)
    c = lst[b]
    if b >= len(lst):
        return -1
    else:
        return c

