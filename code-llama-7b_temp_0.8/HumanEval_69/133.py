
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
    # Find the highest value that appears in the list
    max_value = max(lst)

    # Find the number of times the highest value appears in the list
    highest_count = lst.count(max_value)

    # Check if the highest value appears as many times as or more than itself.
    # If so, return the highest value
    if highest_count >= max_value:
        return max_value
    else:
        return -1
