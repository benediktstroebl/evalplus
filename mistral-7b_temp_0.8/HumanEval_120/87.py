
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
    def heap_sort(arr, k):
        if k > len(arr):
            k = len(arr)
        i = 0
        while i < k:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
        return arr


    def merge(arr, k):
        if len(arr) <= k:
            return arr
        i = k // 2
        left = merge(arr[:i], k)
        right = merge(arr[i:], k)
        return merge_sorted_arrays(left, right)

    def merge_sorted_arrays(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
              
