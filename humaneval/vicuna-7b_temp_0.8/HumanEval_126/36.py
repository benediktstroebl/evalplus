
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
    # handle cases with more than 1 duplicate
    if len(lst) > 1 and any(x == lst[0] for x in lst[1:]) and not any(x == lst[0] for x in lst):
        return False
    # handle case with negative number
    if any(lst[0] < 0):
        return False
    # handle case with float
    if any(float(x) != x for x in lst):
        return False
    # check for duplicates
    duplicates = set(lst)
    if duplicates.len() > 1:
        return False
    if duplicates.len() == 1 and lst.index(duplicates.pop()) != 0:
        return False
    return True