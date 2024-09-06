
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def digit_sum(num):
        """
        Takes a number `num` and returns the sum of its digits.
        >>> digit_sum(0) == 0
        >>> digit_sum(-123) == -6
        >>> digit_sum(123) == 6
        >>> digit_sum(-1) == -1
        """
        if num == 0:
            return 0

        sign = 1
        if num < 0:
            sign = -1
            num *= -1
        return sign * sum(map(int, str(num)))

    return sum(map(lambda num: digit_sum(num) > 0, arr))
