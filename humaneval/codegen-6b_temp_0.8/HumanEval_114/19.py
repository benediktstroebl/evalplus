import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    l = len(nums)
    max_sum = [0] * l
	sum = [0] * l
	for i in range(l):
		sum[i] = nums[i]
		max_sum[i] = sum[i]
	max_sum[0] = nums[0]
	for i in range(1, l):
		max_sum[i] = max(sum[i-1], max_sum[i-1])
		if sum[i] < 0:
			sum[i] = 0
		else:
			sum[i] += nums[i]
	min_sum = min(sum)
	return min_sum
