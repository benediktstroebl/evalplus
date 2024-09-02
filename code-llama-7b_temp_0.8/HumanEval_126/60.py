
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
    
    # if the list is empty
    if len(lst) == 0:
        return True
    
    # if the list has only 1 item
    if len(lst) == 1:
        return True
    
    # if the list has 2 items
    if len(lst) == 2:
        if lst[0] < lst[1]:
            return True
        else:
            return False
    
    # if the list has more than 2 items
    if len(lst) > 2:
        
        # check the first 2 items
        if lst[0] < lst[1]:
            # check the last 2 items
            if lst[1] < lst[2]:
                # run the function again on the rest of the list
                return is_sorted(lst[2:])
            else:
                return False
        else:
            return False
