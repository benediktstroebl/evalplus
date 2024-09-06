import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # We'd want to use two pointers/sliding window, but we can't.
    # We can make a sliding window of at least the size of the array,
    # so that we can search for the min subarray.
    # But the elements in the subarray must be contiguous in the array.
    # And it must begin and end in the array.
    # This means, we are not assuming about the order of the array.
    # We just have to find if there is a subarray that sums to at least 0.
    # The question is, what is the best way to do this.
    # We can divide the problem into simple min subarray sum, and sliding
    # window with suboptimal complexity.
    # We pick the suboptimal complexity, which is to find the smallest
    # subarray, and then another suboptimal complexity to find the second,
    # and so on.
    # We can try the sliding window from the start, and then the end of the array,
    # and do the same for each subarray of the array.
    # This leads to O(n^2) complexity.
    # We can try using a buffer array, which allows us to look ahead
    # and store the elements to the buffer while searching for the subarray.
    # The sliding window can be fairly easy to implement, as it is very similar to the previous question.
    # It only needs a buffer of size, len(nums) - k + 1, to store the elements.
    # Time: O(n^2)
    # Space: O(n)
    if nums is None or len(nums) == 0:
        return 0
    max = -1 * math.inf
    minSum = 0
    for i in range(len(nums)):
        minSum = minSum + nums[i]
        if minSum > max:
            max = minSum
        if minSum == 0:
            return 0
    return max
