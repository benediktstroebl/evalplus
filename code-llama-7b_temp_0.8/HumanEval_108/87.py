
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
    result = 0
    for num in arr:
        sum = 0
        is_negative = num < 0
        num = abs(num)
        while num:
            sum += num % 10
            num //= 10
        if sum > 0 or not is_negative:
            result += 1
    return result
