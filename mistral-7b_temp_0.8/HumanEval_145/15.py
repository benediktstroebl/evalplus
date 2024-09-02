
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
    from math import floor

    def get_sum_of_digits(num: int) -> int:
        return sum([int(i) for i in str(num)])

    ordered = []
    for i in range(len(nums)):
        ordered.append((get_sum_of_digits(nums[i]), i))

    ordered.sort()

    return [nums[i] for (sum, i) in ordered]

