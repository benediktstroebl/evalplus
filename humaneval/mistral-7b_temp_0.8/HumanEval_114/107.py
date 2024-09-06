import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # there are three steps
    # first, find the min sum of the subarray that contains the smallest element
    # second, find the min sum of the subarray that contains the biggest element
    # third, subtract the min sum of the subarray that contains the smallest element
    # from the min sum of the subarray that contains the biggest element
    # the difference is the min sum of the subarray that contains all the elements
    # and the min sum of the subarray is what we are looking for
    n = len(nums)
    smallest = nums[0]
    biggest = nums[0]
    min_sum = nums[0]
    for i in range(1, n):
        smallest = min(smallest, nums[i])
        biggest = max(biggest, nums[i])
        min_sum += nums[i]

    # if the smallest element is not the first element of the array, the min sum is the sum of the elements of the array minus the sum of the smallest element
    if smallest != nums[0]:
        min_sum = min_sum
