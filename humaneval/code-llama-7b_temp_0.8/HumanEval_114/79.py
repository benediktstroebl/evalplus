import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # bad example
    # bad_array = [9, 3, 2, 5, 7, 2, 4]
    # for i in range(len(bad_array)):
    #     for j in range(len(bad_array)):
    #         print(bad_array[i:j])
    #         if bad_array[i:j]:
    #             print(sum(bad_array[i:j]))
    #             break

    # # good example
    # good_array = [9, 3, 2, 5, 7, 2, 4]
    # for i in range(len(good_array)):
    #     print(good_array[i:])
    #     if good_array[i:]:
    #         print(sum(good_array[i:]))
    #         break

    # best example
    min_sub_array_sum = math.inf
    current_sum = 0
    for num in nums:
        current_sum += num
        min_sub_array_sum = min(min_sub_array_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return min_sub_array_sum
