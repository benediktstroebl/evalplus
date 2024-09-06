
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
    def is_int(num):
        try:
            int(num)
            return True
        except ValueError:
            return False
    return sorted(nums, key=lambda x: sum(
        [int(digit) for digit in str(x)]
    ))

