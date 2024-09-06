
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

    # Return empty list if k > len(arr)
    if k > len(arr):
        return []

    # Create a new list to store the k largest elements
    k_largest = []

    # Sort the array in descending order using Python's sorted function
    sorted_arr = sorted(arr, reverse=True)

    # Add the first k elements to the k_largest list
    for i in range(k):
        k_largest.append(sorted_arr[i])

    # Return the k_largest list
    return k_largest
