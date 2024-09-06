
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

    # Write your code here
    # create a variable to store the maximum k numbers
    max_nums = []

    # create a variable to keep track of the current maximum
    current_max = arr[0]

    # add the first element to the maximum k numbers list
    max_nums.append(arr[0])

    # loop through the remaining elements in the array
    for i in range(1, len(arr)):
        # check if the current element is greater than the current maximum
        if arr[i] > current_max:
            # update the current maximum
            current_max = arr[i]

            # if the maximum k numbers list is full, remove the smallest element
            if len(max_nums) == k:
                max_nums.remove(max_nums[0])

            # add the current element to the maximum k numbers list
            max_nums.append(arr[i])

    # return the sorted maximum k numbers list
    return max_nums

