
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
    # The dict and list to keep track of frequency
    frequency = {}
    lst_without_duplicates = []
    
    # First, we populate the frequency and list without duplicates
    for i in lst:
        if i not in lst_without_duplicates:
            lst_without_duplicates.append(i)
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    # Now, we search for the number with frequency equal or greater than itself.
    for key, value in frequency.items():
        if value >= key:
            return key
    return -1
