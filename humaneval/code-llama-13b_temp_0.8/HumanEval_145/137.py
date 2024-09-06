
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
    # 1. Define a function to calculate the sum of the digits
    def sum_of_digits(num):
        """
        Calculate the sum of the digits.
        For example:
        >>> sum_of_digits(11) == 2
        >>> sum_of_digits(111) == 3
        """
        return sum([int(n) for n in str(abs(num))])
    # 2. Sort the list of numbers by the sum of their digits
    return sorted(nums, key=lambda num: (sum_of_digits(num), num))

