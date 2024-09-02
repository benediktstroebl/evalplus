
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
    def smallest_change_helper(arr, start, end):
        if start >= end:
            return 0

        if start + 1 == end:
            return start - arr[start]

        mid = (start + end) // 2
        # if there is no change, the sum is the smallest
        if arr[start] == arr[end]:
            return smallest_change_helper(arr, start + 1, end - 1)

        # there is change, we can either replace arr[mid] with arr[start] for first change
        #  OR replace arr[mid] with arr[end] for second change
        num_changes = smallest_change_helper(arr, start + 1, end - 1)
        if arr[mid] == arr[end]:
            num_changes += smallest_change_helper(arr, start, mid - 1)
        elif arr[mid] == arr[start]:
            num_changes += smallest_change_helper(arr, mid + 1, end)
        return min(num_changes, smallest_change_helper(arr, start, end - 1)) + 1

    return smallest_change_helper(arr, 0, len(arr) - 1)

