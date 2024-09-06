
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
    def merge(arr, arr1, arr2):
        i = 0
        j = 0
        k = 0
        while k < len(arr):
            if i == len(arr1):
                arr[k] = arr2[j]
                j += 1
            elif j == len(arr2):
                arr[k] = arr1[i]
                i += 1
            else:
                if arr1[i] >= arr2[j]:
                    arr[k] = arr1[i]
                    i += 1
                else:
                    arr[k] = arr2[j]
                    j += 1
            k += 1

    if not arr or k == 0 or k > len(arr): return []

    arr1 = sorted(arr[:k])
    arr2 = sorted(arr[k:])
    arr = [0] * len(arr)
    merge(arr, arr1, arr2)

    return arr

