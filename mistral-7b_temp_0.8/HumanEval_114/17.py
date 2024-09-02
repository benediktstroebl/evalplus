
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def minSubArraySum(nums):
        sum, minSum, minSub = 0, 0, 0
        for i in nums:
            sum += i
            if minSub == 0 and sum < 0:
                minSub = sum
            elif sum < minSum:
                minSum = sum
        return minSum
    return minSubArraySum(nums)

