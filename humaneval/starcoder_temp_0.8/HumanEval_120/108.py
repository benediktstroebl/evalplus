
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
    # Brute force O(n log n)
    # return sorted(arr, key=lambda x: -abs(x))[:k]

    # Brute force O(n^2)
    # arr.sort(key=lambda x: -abs(x))
    # return arr[:k]

    # Hash map O(n log n)
    # d = {}
    # for num in arr:
    #     if num in d:
    #         d[num] += 1
    #     else:
    #         d[num] = 1
    # return sorted([k for k, v in d.items()], key=lambda x: -abs(x))[:k]

    # Hash map O(n)
    # d = {}
    # for num in arr:
    #     if num in d:
    #         d[num] += 1
    #     else:
    #         d[num] = 1
    # return sorted(d, key=lambda x: (-d[x], -abs(x)))[:k]

    # Heap O(n log k)
    return sorted(arr, key=lambda x: -abs(x))[:k]
