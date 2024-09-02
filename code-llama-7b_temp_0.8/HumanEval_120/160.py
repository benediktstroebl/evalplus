
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
        pivot = left
        while left < right:
            if arr[left] <= arr[pivot]:
                left += 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                right -= 1
        arr[pivot], arr[right] = arr[right], arr[pivot]
        return right

    def quick_select(arr, left, right, k):
        if left == right:
            return arr[left]
        
        pivot = partition(arr, left, right)

        if pivot == k:
            return arr[k]
        elif pivot > k:
            return quick_select(arr, left, pivot - 1, k)
        else:
            return quick_select(arr, pivot + 1, right, k)

    return sorted(arr[:k]) if k <= len(arr) else sorted(arr[:] + maximum(arr[k - len(arr):], len(arr) - k))
