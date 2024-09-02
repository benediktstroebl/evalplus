
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
    def partition(low, high):
        i, j = low - 1, high + 1
        mid = arr[low + (high - low) // 2]
        while True:
            while True:
                i += 1
                if arr[i] >= mid:
                    break
            while True:
                j -= 1
                if arr[j] <= mid:
                    break
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    def quickSelect(low, high, k):
        if low >= high:
            return arr[low]
        pivot = partition(low, high)
        if pivot == k:
            return arr[pivot]
        elif pivot < k:
            return quickSelect(pivot + 1, high, k)
        else:
            return quickSelect(low, pivot - 1, k)
    
    return quickSelect(0, len(arr) - 1, len(arr) - k)


