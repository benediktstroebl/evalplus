
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
    # sort the list
    lst.sort()
    # i will go through the list from lst.size -1
    # each time i check the current value and the one before
    # if the difference is greater than the current value, i add one to count and return the number
    # if not, i go to the next number
    count = 0
    for i in range(len(lst)-1, 0, -1):
        if lst[i] - lst[i-1] > lst[i]:
            count = count + 1
            return lst[i]
    return -1
