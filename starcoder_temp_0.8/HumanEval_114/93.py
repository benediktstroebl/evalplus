import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sub_array_length = 0
    sub_array_sum = 0
    sum_dict = dict()
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num
        sub_array_length += 1
        sub_array_sum += num

        if sub_array_sum < 0:
            sub_array_sum = 0
            sub_array_length = 0

        elif current_sum in sum_dict:
            # print(sum_dict[current_sum], sub_array_length)
            if sum_dict[current_sum] > sub_array_length:
                sum_dict[current_sum] = sub_array_length

        else:
            sum_dict[current_sum] = sub_array_length

    if len(sum_dict) == 0:
        return 0

    min_length = min(sum_dict.values())
    return min_length * min(sum_dict.keys())
