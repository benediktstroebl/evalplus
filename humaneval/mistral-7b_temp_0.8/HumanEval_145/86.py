
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
        if num < 10:
            return num
        return sum_of_digits(num/10) + num % 10

    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))
