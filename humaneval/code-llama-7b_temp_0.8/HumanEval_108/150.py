
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
    def has_signed_digit(n):
        return n < 0 or n > 0

    def has_positive_sum_of_digits(n):
        digits = str(abs(n))
        total = 0
        for char in digits:
            total += int(char)
        return total > 0

    return sum(
        has_positive_sum_of_digits(n)
        for n in arr
        if has_signed_digit(n)
    )

