
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
    if len(arr) < k:
        return arr

    k_max = arr[0]
    k_max_index = 0
    k_second_max = arr[1]
    k_second_max_index = 1
    k_third_max = arr[2]
    k_third_max_index = 2

    for i in range(3, k):
        if arr[i] > k_max:
            k_third_max = k_second_max
            k_second_max = k_max
            k_max = arr[i]
            k_third_max_index = k_second_max_index
            k_second_max_index = k_max_index
            k_max_index = i
        elif arr[i] > k_second_max:
            k_third_max = k_second_max
            k_second_max = arr[i]
            k_second_max_index = k_max_index
            k_third_max_index = k_second_max_index
        elif arr
