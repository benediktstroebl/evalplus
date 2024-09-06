
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
    n = len(lst)
    # Check for the frequent elements
    max_freq = 0
    max_element, max_freq = -1, 0
    for i in range(n):
        count = 0
        for j in range(n):
            if lst[i] == lst[j] and lst[j] != i:
                count += 1
        if count >= max_freq:
            max_freq = count
            max_element = lst[i]
    return max_element
