
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
    if not lst:
        return -1
    
    count = {}
    for num in lst:
        if num == 0:
            continue
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    count = list(count.items())
    count.sort(key=lambda x: x[0], reverse=True)
    count.sort(key=lambda x: x[1], reverse=True)
    for num, freq in count:
        if freq >= num:
            return num
    return -1
