
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
    n = len(arr)
    k = max(k, 0)

    # Create a list of k copies of the maximum value
    max_list = [max(arr)]

    # Copy the remaining elements to the k copies
    for i in range(k):
        max_list.append(arr[n-1])
        n -= 1

    # Slice the array to the nth copy of the maximum value
    return arr[n-1:n]
