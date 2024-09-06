
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
    # Given a list of positive integers, return the greatest integer that is greater than zero, and has a frequency greater than or equal to the value of the integer itself.
    # If no such a value exist, return -1.
    # Example:
    #     search([4, 1, 2, 2, 3, 1]) == 2
    #     search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    #     search([5, 5, 4, 4, 4]) == -1

    # Step 1: Initialize the maximum value to -1 and the maximum frequency to 0.
    max_val = -1
    max_freq = 0

    # Step 2: Iterate over the list and count the frequency of each element.
    for val in lst:
        freq = lst.count(val)

        # Step 3: If the current element's frequency is greater than or equal to its value, check if it is greater than the maximum value or has a higher
