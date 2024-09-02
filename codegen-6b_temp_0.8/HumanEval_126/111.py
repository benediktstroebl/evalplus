
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
    # Edge Case: If list is empty, return True
    if not lst:
        return True

    # Edge Case: If list has only one item, return True
    if len(lst) == 1:
        return True

    # Edge Case: If list has more than one item and duplicate, return False
    if len(lst) > 1 and lst[0] == lst[-1]:
        return False

    # Edge Case: If list has more than one item and duplicate, return False
    if len(lst) > 1 and lst[0] == lst[-2]:
        return False

    # Edge Case: If list has more than one item and duplicate, return False
    if len(lst) > 1 and lst[0] != lst[-1]:
        # Store values in a set for faster comparison
        a_set = set(lst[0:len(lst)] + lst[-1:len(lst)+1])
        return len(a_set) == len(lst)

    # Edge Case: If list has more than one item and duplicate, return False
    if len(lst) > 1 and lst[0] != lst[-1]:
        return False
