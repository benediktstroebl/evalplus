
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
    N = len(arr)
    if N <= 1:
        return 0

    # O(N^2)
    # for i in range(N):
    #     arr_copy = arr[:i] + arr[i+1:]
    #     if is_palindrome(arr_copy):
    #         return len(arr) - len(arr_copy)

    # O(N^3)
    # return min(smallest_change(arr[:i] + arr[i+1:]) for i in range(N))

    # O(N^3)
    # for i in range(N):
    #     changes = 0
    #     for j in range(N):
    #         if i == j:
    #             continue
    #         if arr[i] == arr[j]:
    #             changes += 1
    #     return changes

    # O(N^2)
    left, right = 0, N - 1
    changes = 0
    while left < right:
        if arr[left] != arr[right]:
            changes += 1
        left += 1
        right -= 1
    return changes

