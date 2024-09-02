
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    if len(arr) == 0:
        return 0

    # Find the most common element
    max_freq = -1
    max_item = None
    for item in set(arr):
        freq = arr.count(item)
        if freq > max_freq:
            max_freq = freq
            max_item = item

    # If the most common element is just one, then we've already
    # made it palindromic
    if max_freq == 1:
        return 0

    # The difference between the max and min is the number of items that need to be
    # changed
    return max_freq - 1

assert smallest_change([1,2,3,5,4,7,9,6]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([]) == 0
