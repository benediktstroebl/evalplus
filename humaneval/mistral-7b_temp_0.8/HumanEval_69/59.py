
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
    # 1. Get the value of the most common number in the list
    most_common_number = max(set(lst), key=lst.count)
    # 2. Return the greatest integer that is greater than 0, and has a frequency greater than or equal to
    # the value of the integer itself
    return most_common_number if lst.count(most_common_number) >= most_common_number else -1
