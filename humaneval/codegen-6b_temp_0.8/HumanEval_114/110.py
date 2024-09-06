import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Use an array to temporarily store all the subarray sums"
    subarray_sums = [0]
    for num in nums:
        subarray_sums.append(num + subarray_sums[-1])
    # sum_so_far = max_ending_here, min_sum = min(max_ending_here, sum_so_far)
    # for i in range(len(nums)):
    #     max_ending_here = max(0, max_ending_here + nums[i])
    #     min_sum = min(max_ending_here, min_sum)
    # return min_sum
    return max(subarray_sums[-1], subarray_sums[-2] - subarray_sums[-1])
