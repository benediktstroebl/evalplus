
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
    arr = [x for x in arr if x >= 0] # remove negative numbers
    arr = sorted(arr, reverse=True) # sort in descending order
    k_indices = [i for i, x in enumerate(arr) if i % k == 0] # find k-th indices
    k_values = arr[k_indices] # get the values in the k-th indices
    k_indices.reverse() # reverse the order of k_indices
    k_values.reverse() # reverse the order of k_values
    return k_values

