def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    
    Example:
    >>> minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    >>> minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = current_sum + num
        if current_sum < 0:
            current_sum = 0
        min_sum = min(min_sum, current_sum)
        max_sum = max(max_sum, current_sum)
    
    return min(min_sum, max_sum)