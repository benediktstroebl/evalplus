
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
    def _partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def _quickselect(arr, low, high, k):
        if low > high:
            return []

        pivot_index = _partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index: pivot_index + 1]
        if pivot_index < k:
            return _quickselect(arr, pivot_index + 1, high, k)
        return _quickselect(arr, low, pivot_index - 1, k)

    return _quickselect(arr, 0, len(arr) - 1, k)

