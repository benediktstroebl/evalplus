
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
    # O(n) time and O(1) space
    start, end = 0, len(arr) - 1
    left_most_odd, right_most_odd = -1, -1
    odds_count = 0
    changes = 0
    while end - start >= 1:
        if arr[start] != arr[end]:
            changes += 1
        if arr[start] % 2 != 0:
            left_most_odd = start
            odds_count += 1
        if arr[end] % 2 != 0:
            right_most_odd = end
            odds_count += 1
        if left_most_odd != -1 and right_most_odd != -1:
            changes -= 1
            left_most_odd, right_most_odd = -1, -1
        start += 1
        end -= 1
    return changes if odds_count < 2 else changes - 1
