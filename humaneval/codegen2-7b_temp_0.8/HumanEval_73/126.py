
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
    def helper(left, right, num_changes, temp_changes, smallest_change):
        if right - left < 1:
            return num_changes
        if arr[left] == arr[right]:
            return helper(left + 1, right - 1, num_changes + 1, temp_changes, smallest_change)
        else:
            temp_changes[num_changes] = arr[left]
            return min(helper(left + 1, right, num_changes + 1, temp_changes, smallest_change),
                       helper(left, right - 1, num_changes, temp_changes, smallest_change))

    return helper(0, len(arr) -
