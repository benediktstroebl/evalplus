
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
    if lst[0]==1:
        return -1
    if lst[0]==0:
        return 0
    max_val = lst[0]
    for i in range(len(lst)):
        if max_val==0:
            max_val=lst[i]
            continue
        if lst[i]>max_val:
            max_val=lst[i]
        if lst[i]==max_val:
            if max_val>0:
                c = lst[i+1:].count(lst[i])
                if c>0:
                    return max_val
    return -1
