
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
    my_dict = dict()
    for item in lst:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1

    for item in my_dict:
        if my_dict[item] >= item and item > 0:
            return item
    return -1

    #print(lst)
    #print(my_dict)

