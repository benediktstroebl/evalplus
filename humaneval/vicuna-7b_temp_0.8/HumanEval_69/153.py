
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
    i = 0
    while i < len(lst)-1:
        if lst[i] < lst[i+1]:
            break
        i += 1
    if i == len(lst)-1:
        return -1
    else:
        for j in range(i+1, len(lst)):
            if lst[j] == lst[i]:
                continue
            frequency = 0
            while lst[j] == lst[i]:
                frequency += 1
                j += 1
            return frequency
