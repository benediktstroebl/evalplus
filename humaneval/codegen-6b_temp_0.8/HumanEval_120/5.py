
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
    def max_k(arr, k):
        if len(arr) == 1:
            return arr
        elif k > len(arr):
            return arr

        n = len(arr)
        mid = n // 2

        left = max_k(arr[:mid], k)
        right = max_k(arr[mid:], k)

        return merge(left, right)

    def merge(arr1, arr2):
        a = []
        n1, n2 = len(arr1), len(arr2)
        i, j = 0, 0

        while i < n1 or j < n2:
            if j >= n2 or (i < n1 and arr1[i] <= arr2[j]):
                a.append(arr1[i])
                i += 1
            else:
                a.append(arr2[j])
                j += 1

        return a

    return max_k(arr, k)

assert([2, 3, 1] == maximum([0, 1, 2, 3, 4], 3))
assert([4, 3, 2] == maximum([-3, -4, 5], 3))
assert([2, 4] == maximum([4, -4, 4], 2))
assert([1] == maximum([-3, 2, 1, 2, -1, -2, 1], 1))