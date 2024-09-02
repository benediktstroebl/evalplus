import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 1. If any element of nums is less than 0, return -1^nums.sum()
    for i in range(len(nums)):
        if nums[i] < 0:
            return -1
    # 2. Sort nums in non-descending order.
    nums.sort()
    # 3. Initialize the sum of sub-arrays to 0.
    sum = 0
    # 4. Initialize a variable to store the current non-empty sub-array.
    curr_sum = nums[0]
    # 5. For each element in nums, append it to the current sub-array.
    while True:
        # 5.1 Append the current element to the current sub-array.
        curr_sum += nums[i]
        # 5.2 If the sub-array is non-empty, update its sum.
        if i + 1 < len(nums):
            curr_sum += nums[i + 1]
        # 5.3 If the sub-array sum is equal to the sum of all sub-arrays,
        # check if the current sub-array is the smallest one.
        if curr_sum == sum:
            smallest = True
            for j in range(i, len(nums)):
                if curr_sum + nums[j] > sum:
                    smallest = False
                    break
            if smallest:
                return sum - curr_sum
        # 5.4 If the sub-array sum is greater than the sum of all sub-arrays,
        # remove the last element from the current sub-array.
        if curr_sum > sum:
            curr_sum -= nums[i]
            i -= 1
            continue
        # 5.5 If the current element is the last element of the array,
        # return the sum of the current sub-array.
        if i == len(nums) - 1:
            return sum - curr_sum
        # 5.6 If the current element is less than the sum of all sub-arrays,
        # return -1.
        if nums[i] < sum:
            return -1
