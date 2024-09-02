
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
    # Check if the list is empty
    if not lst:
        return -1

    # Find the first element in the list
    freq = [0] * (len(lst) + 1)
    freq[0] = 1
    curr_max = lst[0]
    curr_freq = curr_max
    for i in range(1, len(lst)):
        if lst[i] > curr_max:
            curr_max = lst[i]
            curr_freq = curr_freq + 1
        else:
            curr_freq = curr_freq + 1

        # Update the frequency of the current element
        freq[i + 1] = curr_freq

    # Return the maximum element and its frequency
    return curr_max, freq[-1]