
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

    def partition(arr, left, right):
        if left == right:
            return left
        pivot = arr[left]
        for i in range(left+1, right):
            if arr[i] < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        arr[left], arr[right] = arr[right], arr[left]
        return left
    def quick_sort(arr, left, right):
        if left < right:
            mid = partition(arr, left, right)
            quick_sort(arr, left, mid-1)
            quick_sort(arr, mid+1, right)
    left = 0
    right = len(arr)-1
    quick_sort(arr, left, right)
    return arr[:k]

