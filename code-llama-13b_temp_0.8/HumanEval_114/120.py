import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # TODO: Your code here
    # 2 pointers approach O(N)
    minSum = float('inf')
    left, right = 0, 0
    windowSum = 0
    while right < len(nums):
        # add the next element
        windowSum += nums[right]
        # shrink window as much as possible
        while windowSum < minSum and right < len(nums):
            # expand window
            right += 1
            # update minimum sum
            if right - left > 0:
                minSum = min(minSum, windowSum)
        # shrink window by removing nums[left]
        windowSum -= nums[left]
        left += 1
        # print(f'left {left} right {right} minSum {minSum}')
    return minSum

