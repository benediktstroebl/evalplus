
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # You may assume that the answer will fit into a 32-bit signed integer.
    # I think we don't need to handle the case when there is no min sub array sum

    # This is my idea.
    # We can use a hash map to record the sum of each index,
    # then find the minimum sum in the hash map.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # (Notice that the space complexity is for the hash map)

    # I think we can also use a greedy algorithm to find the min sum sub array,
    # here is the code.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # (Notice that the space complexity is for the two variables)

    # def minSubArraySum(nums):
    #     result = nums[0]
    #     sum = 0
    #     for i in range(len(nums)):
    #         sum += nums[i]
    #         if sum >= result:
    #
