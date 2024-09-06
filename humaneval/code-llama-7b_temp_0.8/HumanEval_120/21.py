
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
    def select_top_k(arr, k):
        if not arr: return []

        p = partition(arr, 0, len(arr)-1)
        if p+1 == k:
            return arr[:p+1]
        elif p+1 > k:
            return select_top_k(arr[:p+1], k)
        else:
            return select_top_k(arr[p+1:], k-p-1)

    def partition(arr, left, right):
        pivot = arr[left]
        l, r = left, right

        while l <= r:
            while l <= r and arr[l] <= pivot:
                l += 1
            while l <= r and arr[r] >= pivot:
                r -= 1
            if l < r:
                arr[l], arr[r] = arr[r], arr[l]

        arr[r], arr[left] = arr[left], arr[r]

        return r

    arr = sorted(arr, reverse=True)
    return select_top_k(arr, k)
