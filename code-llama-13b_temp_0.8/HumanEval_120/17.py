
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
    # Find k'th largest element in array.
    n = len(arr)
    k_largest = find_k_largest(arr, n, k)
    # Find k'th smallest element in array.
    k_smallest = find_k_smallest(arr, n, k)
    # k'th largest is equal to k'th smallest.
    if k_largest == k_smallest:
        return [k_largest] * k
    # All elements in array are same.
    elif k_largest == k_smallest and k > 1:
        return [k_largest] * k
    else:
        # Return k'th largest to k'th smallest.
        return [arr[i] for i in range(k_largest, k_smallest + 1)]

