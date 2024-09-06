
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
    if lst == []:
        return -1
    frequency_dict = {}
    frequency = 0
    max_value = -1
    for i in range(len(lst)):
        if lst[i] in frequency_dict:
            frequency_dict[lst[i]] = frequency_dict[lst[i]] + 1
        else:
            frequency_dict[lst[i]] = 1

    for item in frequency_dict:
        if frequency_dict[item] >= item and item >= max_value:
            max_value = item
    return max_value

