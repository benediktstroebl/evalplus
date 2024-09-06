
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
    # Sorting the list
    lst.sort()
    # Checking if the first element is greater than 1
    if lst[0] > 1:
        return -1
    # Checking if the first element has frequency greater than its value
    if lst.count(lst[0]) >= lst[0]:
        return lst[0]
    else:
        return -1

