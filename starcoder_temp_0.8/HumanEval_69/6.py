
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
    # Put all the values into a dictionary with keys being the values and the values being the frequencies
    lst_dict = {}
    for i in lst:
        if i in lst_dict:
            lst_dict[i] += 1
        else:
            lst_dict[i] = 1
    # Check to see if any of the values has more than or equal to its frequency
    for i in lst_dict:
        if lst_dict[i] >= i:
            return i
    return -1
