
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

    def get_sum_of_digits(n):
        s = 0
        abs_n = abs(n)
        while abs_n:
            s += abs_n % 10
            abs_n //= 10
        return s

    return len([x for x in arr if get_sum_of_digits(x) > 0])

