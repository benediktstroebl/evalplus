
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
    # Find the count of each number in the list.
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    # If all numbers in the list are less than zero, return -1.
    if len(count) == 0:
        return -1
    
    # Find the greatest count, and the index of it.
    greatest_count, greatest_index = 0, 0
    for i in range(len(count)):
        if lst[i] > 0 and count[lst[i]] >= lst[i]:
            if count[lst[i]] > greatest_count:
                greatest_count = count[lst[i]]
                greatest_index = i
    return lst[greatest_index]

