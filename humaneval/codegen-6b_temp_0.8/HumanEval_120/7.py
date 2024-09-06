
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
    if k > len(arr):
        return []
    if arr == []:
        return []
    pos = [0] * k
    neg = [0] * k
    result = []
    for num in arr:
        if num > 0:
            pos[0] = num
            for i in range(k - 1):
                if pos[i] <= pos[i + 1]:
                    pos[i + 1] = pos[i]
            pos[-1] = num
            result.append(pos[-1])
        elif num < 0:
            neg[0] = num
            for i in range(k - 1):
                if neg[i] >= neg[i + 1]:
                    neg[i + 1] = neg[i]
            neg[-1] = num
            result.append(neg[-1])
    return result

assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
assert maximum([4, -4, 4], 2) == [4]
assert maximum([2, 1, 2, -1, -2, 1], 1) == [2]
