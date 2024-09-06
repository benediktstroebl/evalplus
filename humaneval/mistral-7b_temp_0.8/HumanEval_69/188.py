
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
    # list = [4, 1, 2, 2, 3, 1]
    # l = sorted(list, reverse=True)
    # print(l)

    if not list:
        return -1

    list = sorted(list, reverse=True)
    max_freq = 0
    for i in range(len(list)):
        if list[i] == 0:
            return -1
        if list[i] > max_freq:
            max_freq = list[i]

    return max_freq
