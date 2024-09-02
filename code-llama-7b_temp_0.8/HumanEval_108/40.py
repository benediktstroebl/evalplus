
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

    def is_positive(num):
        """Is the input positive?"""
        return num > 0

    def get_positive_sum(num):
        """Get the sum of the absolute values of the digits in a positive number."""
        return sum(map(int, str(abs(num))))

    def get_positive_nums(arr):
        """Return positive numbers in a list."""
        return list(filter(is_positive, arr))

    def get_sum_of_digits(arr):
        """Return the sum of the absolute values of the digits in a list of positive numbers."""
        return sum(map(get_positive_sum, get_positive_nums(arr)))

    return get_sum_of_digits(arr)

