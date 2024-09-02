
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
    if len(lst) == 0:
        return -1
    most_common = 1
    common_list = []
    for x in lst:
        count = lst.count(x)
        if count > most_common:
            most_common = count
            common_list = [x]
        elif count == most_common:
            common_list.append(x)
    if most_common > 1:
        return most_common
    else:
        return -1
