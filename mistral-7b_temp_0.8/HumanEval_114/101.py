
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    def minSubArraySum(nums):
        if not nums:
            return 0
        res, min_sum = math.inf, math.inf
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub_sum = sum(nums[i:j+1])
                res = min(sub_sum, res)
                min_sum = min(res, min_sum)

        return min_sum

    return minSubArraySum(nums)
