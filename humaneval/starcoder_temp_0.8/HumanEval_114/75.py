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
        return None
    else:
        # Idea #1
        # return sum(nums) - min(nums)

        # Idea #2
        # n = len(nums)
        # min_sum = sum(nums[:n-1])
        # i, j = 0, 1

        # while j < n:
        #     curr_sum = sum(nums[i:j])
        #     min_sum = min(curr_sum, min_sum)

        #     if curr_sum > min_sum:
        #         i += 1
        #     else:
        #         j += 1

        # return min_sum

        # Idea #3
        # n = len(nums)
        # min_sum = sum(nums)
        # curr_sum = sum(nums[:2])
        # i = 1

        # while i < n - 1:
        #     if curr_sum < min_sum:
        #         min_sum = curr_sum
        #     curr_sum = curr_sum + nums[i+1] - nums[i]
        #     i += 1

        # return min_sum

        # Idea #4
        n = len(nums)
        min_sum = sum(nums)
        curr_sum = sum(nums[:2])

        for i in range(2, n):
            curr_sum = min(curr_sum+nums[i], nums[i])
            min_sum = min(curr_sum, min_sum)

        return min_sum
