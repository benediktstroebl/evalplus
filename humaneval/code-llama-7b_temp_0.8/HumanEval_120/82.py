
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
    # maintain a list of indices with k numbers
    # insertion sort the list
    # find the max element
    # add it to the list of indices
    # repeat the process until the length of the list equals k

    # find the k max numbers in the array
    arr_indices = find_k_max(arr, k)

    # insertion sort the list
    for i in range(k):
        for j in range(i+1, k):
            if arr[arr_indices[j]] > arr[arr_indices[i]]:
                arr_indices[j], arr_indices[i] = arr_indices[i], arr_indices[j]

    return [arr[i] for i in arr_indices]
