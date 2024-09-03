def minSubArraySum(nums):
    """
    Finds the minimum sum of any non-empty subarray.
    Args:
        nums (list): The input list of integers.
    Returns:
        int: Minimum sum of any subarray.
    """
    if not nums:
        return 0  # Handle empty list
    min_sum = float('inf')
    start = 0
    for end in range(len(nums)):
        min_sum = min(min_sum, nums[end])
        # Move the start index until we find a smaller number than min_sum
        while nums[start] > min_sum:
            min_sum = min(min_sum, nums[start])
            start += 1
        # Now min_sum is the minimum sum of the current subarray
        # ending at end and starting at start
    return min_sum