
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
    n = len(arr)

    if n <= k:
        return sorted(arr)

    # for i in xrange(n - k + 1):
    #     # print arr[i:i+k]
    #     if arr[i:i + k].count(max(arr[i:i + k])) == 1:
    #         return arr[i:i + k]

    # arr.sort()
    # return arr[::-1][:k]

    """
    By replacing each number by the next bigger number, the task
    becomes to find the max of these numbers in that subarray.
    """

    res = []
    for i in range(n - k + 1):

        l, r = i, i + k - 1

        while l >= 0 and r < n:

            if arr[l] < arr[r]:
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1

        if l >= 0:
            res.extend(arr[l:i + k - 1])

        if r < n:
            res.append(arr[r])

    return sorted(res)

