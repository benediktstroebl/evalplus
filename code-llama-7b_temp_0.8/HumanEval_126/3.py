
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    
    # initialize variables
    sorted = True
    last = None
    
    # use enumerate to iterate over the list
    for i, num in enumerate(lst):
        
        # if the current value is greater than the last value
        if num > last:
            last = num
        
        # if it is not, the list is not sorted
        else:
            sorted = False
        
        # if we are not at the end of the list and the values are not
        # sorted, break out of the loop
        if i < len(lst)-1 and not sorted:
            break
            
    return sorted
