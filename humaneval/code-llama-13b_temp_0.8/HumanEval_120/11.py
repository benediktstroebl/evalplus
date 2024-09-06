
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
    if len(arr) == 0: return arr

    def swap(i):
        j = i + r.uniform(-1, 1) * (i - i%k)
        arr[i], arr[j] = arr[j], arr[i]

    # Fisher-Yates Algorithm
    # shuffle the first k numbers
    for i in range(k):
        swap(i)
    # sort the first k numbers
    arr[:k] = sorted(arr[:k], reverse=True)
    return arr[:k]

