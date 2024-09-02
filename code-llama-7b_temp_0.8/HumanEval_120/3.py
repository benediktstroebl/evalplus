
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
    def quick_sort(arr, start, end):
        if start >= end:
            return
        pivot = start
        l = start + 1
        r = end
        while l <= r:
            while l <= r and arr[l] <= arr[pivot]:
                l += 1
            while r >= l and arr[r] >= arr[pivot]:
                r -= 1
            if l < r:
                arr[l], arr[r] = arr[r], arr[l]
        arr[pivot], arr[r] = arr[r], arr[pivot]
        quick_sort(arr, start, r - 1)
        quick_sort(arr, r + 1, end)

    quick_sort(arr, 0, len(arr) - 1)
    return arr[:k]

