
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
    def partition(arr, start, end):
        pivot = start
        while start < end:
            while start < end and arr[start] < arr[pivot]:
                start += 1
            while start < end and arr[end] >= arr[pivot]:
                end -= 1
            if start < end:
                arr[start], arr[end] = arr[end], arr[start]
        arr[pivot], arr[end] = arr[end], arr[pivot]
        return end

    def quick_sort(arr, start, end):
        if start < end:
            mid = partition(arr, start, end)
            quick_sort(arr, start, mid - 1)
            quick_sort(arr, mid + 1, end)

    def select_k(arr, k):
        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]
    
    return select_k(arr, k)
