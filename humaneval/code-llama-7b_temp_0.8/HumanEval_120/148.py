
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
    if k <= 0: return []
    n = len(arr)
    if k == n: return sorted(arr)
    if k == 1: return [max(arr)]

    _max = max(arr)
    _min = min(arr)

    # get the number of total buckets
    # each bucket is in charge of one element
    # and two adjacent numbers will be put in the same bucket
    bucket_count = n

    # insert the min and max value into two buckets
    arr.insert(0, _min)
    arr.append(_max)
    bucket_count += 2

    # traverse the buckets, and get the number of each bucket
    # buckets[-1] is the max value in the array
    # buckets[0] is the min value in the array
    # buckets[i] is the number of each bucket
    buckets = [0] * bucket_count

    for i in range(1, len(arr)):
        num = arr[i]
        bucket_idx = buckets[i - 1] - num
        buckets[bucket_idx] += 1

    # build the result array
    res = [None] * k
    result_idx = k - 1

    # traverse the buckets, and the kth number is from the rightmost bucket
    for bucket_idx in range(bucket_count - 2, -1, -1):
        res[result_idx] = buckets[bucket_idx]

        # if the bucket has k numbers, then all the numbers in the bucket are
        # the kth numbers
        if res[result_idx] == k: break

        # if the bucket doesn't have k numbers, then remove the number from the
        # leftmost bucket, which is the bucket of the maximum value in the array
        if res[result_idx] < k:
            result_idx -= buckets[bucket_idx - 1]

    return res

