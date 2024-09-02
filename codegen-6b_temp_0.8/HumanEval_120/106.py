
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
    if k > len(arr): return arr

    def find_max(arr, start):
        max_k = 0
        k = 0
        for i in range(start, len(arr)):
            if arr[i] > max_k:
                k = i
                max_k = arr[i]
        return k

    def helper(arr, k):
        if k == 0: return
        start = 0
        i = 0
        while i < len(arr):
            if arr[i] > arr[start]:
                start = i
            i += 1

        if start != 0:
            max_k = arr[start]
            k -= 1
            arr[start] = arr[find_max(arr, start)]
            arr[start + 1:] = sorted(arr[start + 1:])
            if k > 0:
                for i in range(start, len(arr)):
                    if arr[i] > max_k:
                        arr[i], arr[start] = arr[start], arr[i]
                        helper(arr, k)
    helper(arr, k)
    return arr[:k]

