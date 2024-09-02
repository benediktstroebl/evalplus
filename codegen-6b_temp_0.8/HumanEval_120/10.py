
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
    max_k_nums = [] # the k numbers with the max value to return
    for i in range(k): # iterate through k numbers
        max_v = -sys.maxsize - 1 # initialize the max value to -infinity
        max_v_idx = -1 # initialize the max index to -1
        for j in range(len(arr)):
            if arr[j] > max_v: # if the current value is the max value
                max_v = arr[j] # set the max value to the current value
                max_v_idx = j # set the max index to the current index
        max_k_nums.append(arr[max_v_idx]) # append the max index to the list
        arr.pop(max_v_idx) # pop the current max value
    return max_k_nums
