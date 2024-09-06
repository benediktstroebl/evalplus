
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
    # YOUR CODE HERE
    def sum_of_digits(num):
        """
        Returns the sum of the digits of the integer
        >>> sum_of_digits(123)
        6
        >>> sum_of_digits(-123)
        6
        >>> sum_of_digits(0)
        0
        >>> sum_of_digits(0.5)
        Traceback (most recent call last):
            ...
        TypeError: only integers can be summed
        """
        return sum(int(digit) for digit in str(num))
    return sorted(nums, key=sum_of_digits)


