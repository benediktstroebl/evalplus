
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
    # u[val] == 1 for the first val in lst
    u = {num: 1 for num in lst}
    for num in lst:
        # if not found -1
        if num == -1:
            return -1
        # if u[num] > num then update and return num
        elif u[num] > num:
            return num
        # else update u[num]
        else:
            u[num] += 1
    # if not found -1
    return -1

