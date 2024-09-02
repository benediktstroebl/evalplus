
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
    # Basic case, empty list
    if len(lst) == 0:
        return True

    # If first element of list is not smaller than second, return False
    if lst[0] >= lst[1]:
        return False

    # Recursive case
    # Base case is when the last element is reached in the list
    if len(lst) == 1:
        return True

    # Recursive call
    else:
        # If the next elements are larger than the previous,
        # recursively call the function
        if lst[1] >= lst[0]:
            return is_sorted(lst[1:])
        # Otherwise return False
        else:
            return False

