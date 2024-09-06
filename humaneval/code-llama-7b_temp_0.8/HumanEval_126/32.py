
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
    
    # first check if there's more than 1 dup in the list
    if len(lst) > len(set(lst)):
        return False
    # next check if lst is length 1 or 2
    if len(lst) <= 2:
        return True
    
    # keep slicing the list until you only have 2 items
    while len(lst) > 2:
        if lst[0] > lst[1]:
            return False
        else:
            lst = lst[1:]
    
    # if you get here, you have 2 numbers left and they are sorted
    return True

