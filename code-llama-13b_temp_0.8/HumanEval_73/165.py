
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
    def is_palindrome(arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True

    def count_changes(arr, left, right):
        n = len(arr)
        # check all values from left to right are same.
        for i in range(left, right + 1):
            if arr[i] != arr[left]:
                return n - right - 1

        # check all values from right to left are same.
        for i in range(right - 1, left - 1, -1):
            if arr[i] != arr[right]:
                return n - right - 1

        # Check left == right.
        if left == right:
            return 0
        return count_changes(arr, left + 1, right - 1)

    n = len(arr)
    if n == 1:
        return 0

    # check if array is already palindrome.
    if is_palindrome(arr):
        return 0

    # Recurse on all indexes and check count_changes.
    # if no element can make array palindrome then return n.
    return min(count_changes(arr, left, left) for left in range(0, n))

