import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Solution 1: prefix sum
    # Time Complexity: O(n), Space Complexity: O(n)
    if len(nums) < 1:
        return 0
    sums = [0]
    for num in nums:
        sums.append(sums[-1] + num)
    for i in range(1, len(sums)):
        if sums[i] < sums[i - 1]:
            return sums[i]
    return sums[len(sums) - 1]

    # Solution 2: sliding window
    # Time Complexity: O(n), Space Complexity: O(1)
    sums = 0
    min_sum = float('inf')
    left, right = 0, 0
    while right < len(nums):
        sums += nums[right]
        if right - left + 1 < 2:
            right += 1
            continue
        if sums < min_sum:
            min_sum = sums
        if sums >= 0:
