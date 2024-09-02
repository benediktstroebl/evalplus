
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
    if not lst:
        return -1

    lst.sort()
    start = 0
    end = len(lst) - 1

    if lst[end] == 1:
        return -1
    if lst[start] > lst[end] // 2:
        return lst[start]
    while start + 1 < end:
        mid = (start + end) // 2
        if lst[mid] > lst[mid] // 2:
            return lst[mid]
        if lst[mid] == lst[start] and lst[mid] == lst[end]:
            start += 1
            end -= 1
        else:
            if lst[mid] > lst[start]:
                start = mid
            else:
                end = mid
    return lst[start]


