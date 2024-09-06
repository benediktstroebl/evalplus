def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of nums.
    """
    if not nums:
        return 0  # Empty array, sum is 0
    min_sum = nums[0]  # Initialize min_sum with the first element
    for i in range(1, len(nums)):
        # Calculate the sum of the current element and the minimum sum so far
        cur_sum = nums[i] + min_subarray_sum
        # Update min_sum if the current element contributes a smaller sum
        if cur_sum < min_sum:
            min_sum = cur_sum
    return min_sum
nums = [2, 3, 4, 1, 2, 4]