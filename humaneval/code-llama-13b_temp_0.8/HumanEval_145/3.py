
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # end_index = len(nums) - 1
    # for i in range(0, len(nums)):
    #     for j in range(0, len(nums)):
    #         if sum_digits(nums[i]) == sum_digits(nums[j]) and i < j:
    #             temp = nums[i]
    #             nums[i] = nums[j]
    #             nums[j] = temp
    #             end_index -= 1
    #     end_index -= 1
    # return nums
    return sorted(nums, key=lambda x: (sum_digits(x), x))
