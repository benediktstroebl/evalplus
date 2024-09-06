
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
    def partition(arr, left, right, pivot):
        arr[pivot], arr[right] = arr[right], arr[pivot]
        j = left
        for i in range(left, right):
            if arr[i] <= arr[right]:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        arr[j], arr[right] = arr[right], arr[j]
        return j

    def quickselect(arr, left, right, k):
        if left < right:
            pivot = partition(arr, left, right, right - 1)
            if k <= pivot:
                quickselect(arr, left, pivot - 1, k)
            elif k > pivot:
                quickselect(arr, pivot + 1, right, k)

    n = len(arr)
    quickselect(arr, 0, n - 1, n - k)
    return arr[n - k:]
