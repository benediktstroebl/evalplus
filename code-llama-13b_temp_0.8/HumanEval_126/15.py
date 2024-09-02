
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
    # First check that the list is of a minimum length.
    if len(lst) < 2:
        return True

    # If the list is of a minimum length, loop through the list
    # using the enumerate function.
    for index, number in enumerate(lst):
        # Check that the current index is not out of the list's range.
        # Then check that the next index is also not out of the list's range.
        if index < (len(lst) - 1) and index + 1 < (len(lst)):
            # If the current number is larger than the next number,
            # return False.
            if number > lst[index + 1]:
                return False

    # If all the checks pass, return True.
    return True

