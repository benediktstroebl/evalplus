import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    length = len(nums)
    if length == 0:
        return 0

    min_sub_array_sum = math.inf
    min_sub_array_left = -1

    for i in range(length):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] < nums[i-1]:
            continue

        left = i
        right = i
        sub_array_sum = nums[i]

        while right < length and nums[right] >= 0:
            right += 1
            sub_array_sum += nums[right]

        if sub_array_sum < min_sub_array_sum:
            min_sub_array_sum = sub_array_sum
            min_sub_array_left = left

    return min_sub_array_sum if min_sub_array_sum!= math.inf else 0
