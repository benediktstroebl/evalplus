
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
    if not lst or not isinstance(lst, list):
        return -1
    
    if len(lst) == 1:
        return lst[0]
    
    lst.sort()
    
    for i in range(len(lst)):
        if lst[i] > 0 and lst[i] >= lst[i - 1]:
            j = i - 1
            count = 0
            while j >= 0 and lst[j] == lst[i]:
                j -= 1
                count += 1
            
            if count >= lst[i]:
                return lst[i]
            
    return -1
