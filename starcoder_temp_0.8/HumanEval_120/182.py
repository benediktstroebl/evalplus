
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

    # Edge case
    if len(arr) == 1:
        return arr

    # Bucket sort implementation
    max_num = max(arr)
    min_num = min(arr)
    bucket_size = (max_num - min_num) // k
    bucket = [[] for _ in range(k)]

    for n in arr:
        bucket[(n - min_num) // bucket_size].append(n)

    for i in range(k):
        if len(bucket[i]) > 0:
            bucket[i].sort(reverse=True)

    res = []
    for i in range(k):
        res.append(bucket[i][0])

    return res

