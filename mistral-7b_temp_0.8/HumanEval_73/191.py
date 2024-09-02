
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
    # O(N)
    def count(i, j):
        if j > i:
            return 0
        if j < i:
            return float('inf')

        return abs(arr[j] - arr[i])

    def solve(i, j):
        if i == N-1:
            return 0
        ans = float('inf')
        for k in range(i, j):
            ans = min(ans, solve(i, k) + solve(k+1, j) + count(i, k) + count(k+1, j))
        return ans

    return solve(0, N-1)
