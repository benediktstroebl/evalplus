
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
    # Use the cumulative sum of the digits
    # to keep track of the sum of digits of current number
    for i, n in enumerate(nums):
        sum_digits = 0
        while n > 0:
            digit = n % 10
            n = n // 10
            sum_digits += digit
        nums[i] = sum_digits

    return nums

