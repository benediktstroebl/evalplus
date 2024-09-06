import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    sum_array = []
    subarray = []

    for i in nums:
        subarray.append(i)
        subarray_sum = sum(subarray)
        sum_array.append(subarray_sum)
        #print("Sum of subarray {} is {}".format(subarray, subarray_sum))
        if subarray_sum < 0:
            subarray = []
            continue
        elif subarray_sum == 0:
            subarray = []
            continue
        else:
            continue

    return min(sum_array)

