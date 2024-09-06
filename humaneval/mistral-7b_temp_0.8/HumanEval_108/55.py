
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
    def add_digits(num):
        if num < 0:
            return -num
        if num == 0:
            return 0
        result = 0
        while num > 0:
            result += num % 10
            num //= 10
        return result
    result = 0
    for item in arr:
        if add_digits(item) > 0:
            result += 1
    return result




















































































































































