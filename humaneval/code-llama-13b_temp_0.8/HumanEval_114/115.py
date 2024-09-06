import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # find the smallest value in sub-array, i.e. the value at an index k,
    # for 0 <= k < n, where n is the length of the array
    # For each index k, we should check the sub-arrays with length 1 to n - k,
    # where n - k is the maximum length of the sub-array.
    # The minimum sub-array sum should be the smallest value in the sub-array
    # so we should return this value.
    # Therefore, the time complexity is O(n^2)
    # However, we could improve the time complexity to O(n) by using a sliding window

    # First, we check if the array is empty
    if len(nums) == 0:
        return 0

    # Second, we check if the array is of length 1
    if len(nums) == 1:
        return nums[0]

    # Initialise the minimum sum to be a very large number
    min_sum = math.inf

    # For each index k, we should check the sub-arrays with length 1 to n - k
    for k in range(len(nums)):
        # Initialise the sub-array sum to be 0
        sub_array_sum = 0

        # For each length from 1 to n - k
        for i in range(k, len(nums)):
            # Add the value at index i to the sub-array sum
            sub_array_sum += nums[i]

            # Update the minimum sub-array sum if the current sub-array sum is smaller than it
            if sub_array_sum < min_sum:
                min_sum = sub_array_sum

    return min_sum

