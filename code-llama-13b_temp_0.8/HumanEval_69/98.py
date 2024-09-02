
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

    maxFreq = 0
    val = lst[0]
    for i in range(0, len(lst)):
        if lst[i] > val and lst.count(lst[i]) >= lst[i]:
            val = lst[i]
            maxFreq = lst.count(lst[i])
    
    if maxFreq >= lst[0]:
        return lst[0]
    return val
