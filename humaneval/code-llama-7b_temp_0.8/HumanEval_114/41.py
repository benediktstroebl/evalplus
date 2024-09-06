import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return None

    min_sum = None
    min_sum = float('inf')
    start_index = 0
    end_index = 0
    sum_array = []
    for i in nums:
        sum_array.append(i)

    # print(sum_array)

    while (end_index < len(nums)):
        sum_array[end_index] += sum_array[end_index - 1]
        end_index += 1

    # print(sum_array)

    for i in range(len(sum_array)):
        if sum_array[i] < min_sum:
            min_sum = sum_array[i]

    return min_sum
