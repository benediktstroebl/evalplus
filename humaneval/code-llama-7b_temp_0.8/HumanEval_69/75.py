
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

    # find the maximum element in the list
    # iteratively reduce the list to this max element
    # find the index of max element in the new list
    # return the number of occurrences of the max element in the list

    max_value = lst[0]
    for i in range(len(lst)):
        if lst[i] >= max_value:
            max_value = lst[i]
    reduced_list = lst[:]
    while max_value in reduced_list:
        reduced_list.remove(max_value)
    if reduced_list.count(max_value) >= max_value:
        return max_value
    return -1

