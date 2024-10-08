
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

    def sum_digits(n):
        res = 0
        while n > 0:
            res += n % 10
            n //= 10
        return res

    # Write your code here
    res = 0
    for n in arr:
        if sum_digits(n) > 0:
            res += 1

    return res

