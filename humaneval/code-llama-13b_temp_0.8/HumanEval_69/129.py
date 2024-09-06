
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

    dict_of_ints = {}
    for i in lst:
        if i in dict_of_ints:
            dict_of_ints[i] += 1
        else:
            dict_of_ints[i] = 1
    
    sorted_dict_of_ints = dict_of_ints.items()
    sorted_dict_of_ints.sort()
    sorted_dict_of_ints = sorted_dict_of_ints[::-1]
    
    for i in sorted_dict_of_ints:
        if i[0] <= i[1]:
            return i[0]
    return -1
