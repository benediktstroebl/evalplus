
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    def partition(arr, l, r, pivot):
        idx = l
        for i in range(l, r):
            if arr[i] >= pivot:
                arr[idx], arr[i] = arr[i], arr[idx]
                idx += 1

        arr[idx], arr[r] = arr[r], arr[idx]
        return idx

    def max_subsequence(arr, l, r, k):
        if l > r:
            return []
        if k == 0:
            return []
        if l == r:
            return arr[l]

        pivot = arr[r]
        idx = partition(arr, l, r, pivot)
        # idx - k, len(arr) - 1
        if idx - k >= 0:
            return max_subsequence(arr, l, idx - 1, k)
        if idx - k < 0:
            return max_subsequence(arr, idx + 1, r, k - idx + k)

    arr.sort()
    arr.reverse()
    return max_subsequence(arr, 0, len(arr) - 1, k)

