
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
    if nums == []:
        return []
    else:
        for i in range(0, len(nums)):
            digit_sum = 0
            num_to_check = nums[i]
            for j in range(0, len(str(num_to_check))):
                digit_sum += int(str(num_to_check)[j])
            nums[i] = (digit_sum, nums[i])
        nums.sort()
        for i in range(0, len(nums)):
            nums[i] = nums[i][1]
        return nums

