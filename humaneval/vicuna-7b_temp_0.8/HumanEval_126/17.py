
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
    # This is the same as the Python solution, but with some changes
    # to make it more concise and efficient

    # Check for an empty list
    if not lst:
        return False

    # Check for a single number in the list
    if isinstance(lst[0], int) and lst[0] <= max(lst):
        return True

    # Check for multiple duplicates of a single number in the list
    num_seen = 0
    for num in lst:
        if isinstance(num, int) and num <= max(lst) and (num_seen == 1 or num != lst[num_seen - 1]):
            return False
        num_seen += 1

    # If we reach this point, then the list is sorted
    return True
