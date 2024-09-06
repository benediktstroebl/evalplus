
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
    # if k is larger than the size of the array, return a list with the elements of the array
    if k > n:
        return arr
    # create a list to store the maximum k numbers in the array
    max_k_nums = []
    # create a list to store the indexes of the maximum k numbers in the array
    max_k_indexes = []
    # loop through the array
    for i in range(n):
        # if the value at the current index is larger than the value at the last index in the list of maximum k numbers
        # add the current index to the list of maximum k indexes
        if arr[i] > arr[max_k_indexes[-1]]:
            max_k_indexes.append(i)
            # add the current value to the list of maximum k numbers
            max_k_nums.append(arr[i])
        # if the size of the list of maximum k indexes is equal to k, break the loop
        if len(max_k_indexes) == k:
            break
    
