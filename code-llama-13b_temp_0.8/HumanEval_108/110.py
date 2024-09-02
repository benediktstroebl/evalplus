
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

    def digits(n):
        if n < 0:
            return digits(abs(n))
        elif n < 10:
            return [n]
        else:
            return digits(n // 10) + [n % 10]

    return len([n for n in arr if sum(digits(n)) > 0])

