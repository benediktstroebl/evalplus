
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
    def is_signed_digit(x):
        return x in [1, -1]

    def is_positive(x):
        return x > 0

    def sum_of_digits(x):
        if is_signed_digit(x):
            return x

        digits = [int(d) for d in str(x)]
        return sum(digits)

    def has_positive_sum(x):
        return is_positive(sum_of_digits(x))

    return len([x for x in arr if has_positive_sum(x)])

