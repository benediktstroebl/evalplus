
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
    def sum_of_digits(num):
        sum_ = 0
        while num > 0:
            sum_ += num % 10
            num = num // 10
        return sum_

    def order_nums(a, b):
        return sum_of_digits(a) > sum_of_digits(b)

    return sorted(nums, key=order_nums)

