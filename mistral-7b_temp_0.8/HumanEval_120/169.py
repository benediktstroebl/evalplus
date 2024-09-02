
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

    # Initialize the maximum array
    max_arr = [-float("inf")] * k
    # Initialize the maximum array
    max_arr = [0] * k

    # Iterate over the elements of the input array
    for i in range(len(arr)):
        # If the current element is greater than the maximum array
        if arr[i] > max_arr[0]:
            # Update the maximum array
            max_arr[0] = arr[i]

    # Sort the maximum array in descending order
    max_arr.sort(reverse=True)

    # Return the sorted maximum array
    return max_arr
