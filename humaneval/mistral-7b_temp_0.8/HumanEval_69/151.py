
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
    max1 = -1
    max2 = -1
    counter = 0
    for i in lst:
        if i > max1:
            max2 = max1
            max1 = i
            counter = 1
        elif i == max1:
            counter += 1
        elif i == max2:
            counter += 1
    if counter >= max1:
        return max1
    else:
        return -1

