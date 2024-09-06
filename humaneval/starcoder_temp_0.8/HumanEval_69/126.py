
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
    # Get the frequency of each element in the list
    lst_counts = Counter(lst)
    # Loop through each element and return the first one greater than zero, and with frequency greater than or equal to the value of the integer itself
    for num, count in lst_counts.items():
        if num > 0 and count >= num:
            return num
    # If no such a value exist, return -1
    return -1
