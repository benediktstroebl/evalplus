
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
    from collections import Counter

    if len(arr) == 0 or len(arr) == 1:
        return 0

    counts = Counter(arr)

    odds = 0
    for c in counts:
        if counts[c] % 2 != 0:
            odds += 1

    return min(odds, len(arr) - odds)

assert smallest_change([1,2,3,5,4,7,9,6]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([1,2,3,1,2,3]) == 3
assert smallest_change([4,5,5,1,2,1,2]) == 2
assert smallest_change([4,5,5,5,1,2,1,2]) == 1

