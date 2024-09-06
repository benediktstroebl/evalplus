
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
    mid = lst[0]
    l = 0
    r = len(lst) - 1
    while l <= r:
        mid = (l + r) // 2
        if mid == 0 or lst[mid - 1] <= lst[mid]:
            return lst[mid]
        elif lst[mid] < mid:
            l = mid + 1
        elif mid > 0 and lst[mid - 1] > lst[mid]:
            r = mid - 1
    return -
