
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

    def digit_sum(n):
        if n < 0:
            n = -n
        if n < 10:
            return n
        else:
            return (n % 10) + digit_sum(n // 10)

    count = 0
    for i in arr:
        if digit_sum(i) > 0:
            count += 1
    return count

