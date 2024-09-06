
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
    if len(nums) == 0:
        return []

    sum_nums = [0]*len(nums)
    sum_nums_origin = [0]*len(nums)

    for i in range(len(nums)):
        num = nums[i]
        num_sum = 0
        while num:
            num_sum += num % 10
            num //= 10
        sum_nums[i] = num_sum

    sorted_sum_nums = sorted(sum_nums)

    for i in range(len(sum_nums)):
        sum_nums[i] = sorted_sum_nums.index(sum_nums[i])

    for i in range(len(sum_nums)):
        for j in range(len(sum_nums)):
            if sum_nums[i] == sum_nums[j]:
                sum_nums_origin[i] = nums[j]

    for i in range(len(sum_nums)):
        nums[i] = sum_nums_origin[i]

    return nums

