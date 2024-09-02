
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
    lst_set = set(lst)
    lst_dict = dict()
    for n in lst:
        if n not in lst_dict:
            lst_dict[n] = 1
        else:
            lst_dict[n] += 1

    for n in lst_dict:
        if lst_dict[n] > n:
            return n
    return -1
