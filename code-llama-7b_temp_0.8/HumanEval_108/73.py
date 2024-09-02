
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
    if len(arr) == 0:
        return 0

    count = 0
    for n in arr:
        is_positive = True
        if n < 0:
            is_positive = False
        n = abs(n)
        total_sum = 0
        while n > 0:
            digit = n % 10
            total_sum += digit
            n //= 10
        if total_sum > 0:
            count += 1
    return count

