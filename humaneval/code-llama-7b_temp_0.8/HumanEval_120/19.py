
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
    if not arr:
        return arr

    n = len(arr)
    if n == k:
        return arr

    # i: current max, j: next max
    # pick k numbers of next max
    # if next max < i, swap j and i
    # else if j < k, add j to bucket

    i = k - 1
    j = i
    while i > 0 and j < n - 1:
        i -= 1
        j += 1
        if arr[j] > arr[i]:
            arr[i], arr[j] = arr[j], arr[i]

    return arr[:k]

