
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

    # First, we need to assume the list is sorted.
    # Then, we iterate through the list, while counting
    # the number of consecutive duplicates.
    # Then we check to see if our count is greater than 1.
    # If it is, we return false. If not, we return true.
    # We also have to make sure we don't return true if there
    # are no numbers in the list.

    count = 0
    if len(lst) == 0:
        return False
    else:
        for i in range(len(lst)):
            if lst[i] == lst[i - 1]:
                count += 1
            else:
                count = 0
            if count > 1:
                return False
        return True


