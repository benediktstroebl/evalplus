
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
    index = [0] * len(nums)
    for i, num in enumerate(nums):
        digit = sum(num // i for i in range(len(num)))
        index[digit] += 1
        if index[digit] > 0:
            num = -num
        if len(nums) > 1:
            if nums[0] == num:
                nums = [i for i in nums[1:] if i != num]
            else:
                nums = [i for i in nums if i != num]
        if len(nums) == 0:
            return []
        nums = [nums[i] for i in index.index(max(index))]
    return nums
