
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
    # YOUR CODE HERE
    # Returns the number of elements that need to be changed to make the array palindromic.
    # If the array is already palindromic, return 0.
    def is_palindromic(arr):
        for i in range(len(arr)//2):
            if arr[i] != arr[len(arr) - 1 - i]:
                return False
        return True
    def count_changes(arr, idx, max_changes, dp):
        if idx == len(arr):
            return 0

        if dp[idx] != -1:
            return dp[idx]

        min_changes = float('inf')
        for i in range(idx, len(arr)):
            if arr[idx] != arr[i]:
                changes = count_changes(arr, i + 1, max_changes, dp) + 1
                if changes <= max_changes:
                    min_changes = min(min_changes, changes)

        if min_changes == float('inf'):
            min_changes = 
