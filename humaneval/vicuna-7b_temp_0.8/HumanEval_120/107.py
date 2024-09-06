
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
    # Sort the array in non-increasing order
    arr = sorted(arr, reverse=True)

    # Initialize variables to keep track of the maximum value and its index
    max_value = arr[0]
    max_index = 0

    # Find the maximum value and its index
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i

    # Slice the array to get the maximum k values
    max_values = arr[max_index:max_index+k]

    # Return the sorted list of the maximum k values
    return max_values
