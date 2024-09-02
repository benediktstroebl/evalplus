
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
    # Instantiate two variables to track the minimum and maximum values.
    # Then loop through the list and check if the current value is greater
    # than the minimum value or less than the maximum value.
    # If true, return False. Otherwise, return True.
    if len(lst) < 2:
        return True
    max_val = lst[0]
    min_val = lst[0]
    for i in lst[1:]:
        if i < min_val:
            return False
        if i > max_val:
            max_val = i
            if i < min_val:
                min_val = i
    return True
