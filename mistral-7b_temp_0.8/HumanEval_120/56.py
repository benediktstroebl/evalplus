
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
    # Binary search for the position of the maximum element
    lo, hi = 0, len(arr) - k
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] >= arr[mid + 1]:
            hi = mid
        else:
            lo = mid + 1

    # The first k elements are not in non-increasing order
    # so we need to compare them again to get the maximum k elements
    max_k = [arr[hi]]
    for i in range(hi + 1, hi + k):
        if arr[i] > arr[hi]:
            max_k.append(arr[i])

    max_k.sort()
    return max_k


