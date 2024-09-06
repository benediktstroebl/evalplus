
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Time complexity: O(N)
    # Space complexity: O(1)
    def minSubArraySum(nums):
        subsum, min_subsum = 0, math.inf
        for num in nums:
            subsum += num
            while subsum > nums[0]:
                subsum -= nums[0]
                min_subsum = min(min_subsum, subsum)
            min_subsum = min(min_subsum, subsum)
        return min_subsum

    # Time complexity: O(N)
    # Space complexity: O(N)
    def minSubArraySum2(nums):
        min_subsum = math.inf
        for num in nums:
            min_subsum = min(min_subsum, num)
        for i in range(len(nums)-1, 0, -1):
            nums[i] += nums[i-1]
        for i in range(1, len(nums)):
            min_subsum = min(min_subsum, nums
