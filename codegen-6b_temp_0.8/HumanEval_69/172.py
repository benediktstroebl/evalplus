
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
    lst = lst + [0]
    count = {}
    for num in lst:
        if num not in count:
            count[num] = 0
        count[num] += 1
    max_value = max(count.values())
    for num in count:
        if count[num] == max_value:
            return num
    return -1
