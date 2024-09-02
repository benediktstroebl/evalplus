
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

    if not arr: return []

    def partition(arr, start, end):
        pivot = arr[end]
        i = start
        for j in range(start, end):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[end] = arr[end], arr[i]
        return i

    def quicksort(arr, start, end):
        if start >= end: return

        i = partition(arr, start, end)
        quicksort(arr, start, i - 1)
        quicksort(arr, i + 1, end)

    quicksort(arr, 0, len(arr) - 1)
    return arr[:k]


