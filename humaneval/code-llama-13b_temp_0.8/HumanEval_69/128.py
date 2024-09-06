
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
    # your code
    if not lst or not isinstance(lst, list):
        return -1

    from collections import Counter
    count_dict = Counter(lst)
    maximum = 0
    result = -1

    for value in lst:
        if value >= 1 and count_dict[value] >= value:
            if value > maximum:
                maximum = value
                result = value

    return result
