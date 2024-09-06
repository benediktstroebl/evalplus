
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

    # 2nd attempt
    def solve(arr, i, j):
        if i == j:
            return 0
        if j - i == 1:
            if arr[i] == arr[j]:
                return 0
            else:
                return 2
        mid = (i + j) // 2
        total = 0
        if arr[mid]!= arr[i] and arr[mid]!= arr[j]:
            total += 3
        total += solve(arr, i, mid)
        total += solve(arr, mid + 1, j)
        return total

    return solve(arr, 0, len(arr) - 1)

