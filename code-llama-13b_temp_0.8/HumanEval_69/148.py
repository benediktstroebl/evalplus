
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
    elif len(lst) == 1:
        return lst[0]

    lst.sort()
    num_max = max(lst)
    num_max_count = lst.count(num_max)
    if num_max_count < num_max:
        return -1
    return num_max



