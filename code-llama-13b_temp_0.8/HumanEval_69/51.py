
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
    # converting list to dict to check for the frequency of each number
    lst_dict = dict(Counter(lst))

    # looping through each key and value in the dict to check the condition
    for key, value in lst_dict.items():
        if value >= key:
            # if condition is true
            # the function will return the number that matches the condition
            return key

    # if condition is not met
    return -1

