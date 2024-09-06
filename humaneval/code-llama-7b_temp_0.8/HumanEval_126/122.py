
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
    
    '''
    My strategy:
    1. If the list is empty or has only 1 element, return True
    2. If there are duplicates, return False
    3. For the first two items in the list, check that they are in ascending order
    4. Check that the remaining items are in ascending order
    '''

    # 1
    if len(lst) == 0 or len(lst) == 1:
        return True

    # 2
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            return False

    # 3
    if lst[1] > lst[0]:
        is_ascending = True
    else:
        is_ascending = False

    # 4
    for i in range(2, len(lst)):
        if lst[i] < lst[i-1]:
            is_ascending = False

    return is_ascending

