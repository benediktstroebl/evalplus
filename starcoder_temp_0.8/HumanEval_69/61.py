
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
    # YOUR CODE HERE
    if not lst:
        return -1
    else:
        highest = 0
        highest_count = 0
        for i in lst:
            if i > highest:
                highest = i
                highest_count = 0
            elif i == highest:
                highest_count += 1
        if highest_count >= highest:
            return highest
        else:
            return -1
