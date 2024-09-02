
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
    def nth_element(arr, n, k):
        """find the kth element in arr"""
        if k >= len(arr): return None
        l, r = 0, len(arr)-1
        while l <= r:
            # partition the array into three parts
            # left < pivot < right
            pivot_i = partition(arr, l, r)
            if pivot_i > k:
                r = pivot_i - 1
            elif pivot_i < k:
                l = pivot_i + 1
            else:
                return pivot_i

    def partition(arr, l, r):
        pivot = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

    if not arr or len(arr) == 0: return None
    if len(arr) <= k: return sorted(arr)

    nth = k-1
    arr = arr[:k]
    nth_element(arr, 0, nth)
    return sorted(arr)

