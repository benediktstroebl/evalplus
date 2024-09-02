
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
    def partition(arr, l, r):
        i, j = l, r
        while i < j:
            while arr[i] < arr[l]:
                i += 1
            while arr[j] >= arr[l]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[j] = arr[j], arr[l]
        return j

    def sort_max(arr, l, r, k):
        if k == 0: return 

        j = partition(arr, l, r)
        if j - l < r - j:
            sort_max(arr, l, j, k - 1)
            sort_max(arr, j + 1, r, k - 1)
        else:
            sort_max(arr, j + 1, r, k - 1)
            sort_max(arr, l, j, k - 1)

    sort_max(arr, 0, len(arr) - 1, k)
    return arr[:k]
