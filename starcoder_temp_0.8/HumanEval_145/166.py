
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

    def sort(nums):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum_digits(nums[i]) > sum_digits(nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]

    sort(nums)
    return nums

