
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
    # first we need to check for a list of zeros and return -1
    if min(lst) == 0:
        return -1
    # now we need to sort the list
    lst = sorted(lst)
    # now we need to go through the list and check for each element
    for idx, el in enumerate(lst):
        if idx == len(lst) - 1:
            return -1
        if el == lst[idx + 1]:
            continue
        if el > lst[idx + 1]:
            return el
    return -1
