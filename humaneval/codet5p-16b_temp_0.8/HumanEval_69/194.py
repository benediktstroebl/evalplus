
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

    counter = {}
    for elem in lst:
        if elem not in counter:
            counter[elem] = 1
        else:
            counter[elem] += 1

    max_frequency = -1
    max_frequency_elem = -1
    for elem in counter:
        if counter[elem] > max_frequency:
            max_frequency = counter[elem]
            max_frequency_elem = elem

    return max_frequency_elem if max_frequency_elem > 0 else -1
