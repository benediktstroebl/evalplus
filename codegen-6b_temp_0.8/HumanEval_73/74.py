
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
    min_changes = len(arr)
    arr = [abs(x) for x in arr]
    for i in xrange(len(arr)):
        left = i
        right = len(arr) - 1 - i
        while left < right:
            left_diff = arr[left] - arr[i]
            right_diff = arr[right] - arr[i]
            if left_diff == right_diff:
                if left_diff < min_changes:
                    min_changes = left_diff
                break
            elif left_diff < right_diff:
                left += 1
            else:
                right -= 1

    if min_changes == len(arr):
        return 0
    else:
        return min_changes

