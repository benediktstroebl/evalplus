
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
    count = {int(x):0 for x in lst}
    for x in lst:
        count[x] += 1
    max_val = max(count)
    max_freq = max_val
    for k, v in count.items():
        if v >= max_val:
            max_val = v
            max_freq = k
    return max_freq

lst = [1, 2, 2, 3, 1]
