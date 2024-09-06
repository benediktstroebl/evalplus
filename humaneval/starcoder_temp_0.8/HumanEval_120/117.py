
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
    def partition(arr, l, r, k):
        """
        Returns the index of the pivot element
        """
        pivot = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

    def quick_select(arr, l, r, k):
        if l == r:
            return arr[l]
        # partition the array with pivot index
        pivot_index = partition(arr, l, r, k)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quick_select(arr, l, pivot_index - 1, k)
        else:
            return quick_select(arr, pivot_index + 1, r, k)

    return quick_select(arr, 0, len(arr) - 1, k - 1)

