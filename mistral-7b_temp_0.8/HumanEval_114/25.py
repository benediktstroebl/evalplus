import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    window_size = len(nums)
    min_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, window_size):
        # print("i: ", i, "current sum: ", current_sum, "nums[i]: ", nums[i])
        # print("current sum: ", current_sum, "nums[i]: ", nums[i])
        if nums[i] < 0:
            current_sum = nums[i]
            continue
        else:
            current_sum += nums[i]
            if current_sum < min_sum:
                min_sum = current_sum

        # if current_sum < 0:
        #     #print("zero: ", current_sum)
        #     #print("zero: ", current_sum)
        #     current_sum = 0
        # elif current_sum < min_sum:
        #     min_sum = current_sum

    return min_sum
