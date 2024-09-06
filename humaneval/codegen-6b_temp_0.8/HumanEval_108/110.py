
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
        if num < 0:
            num = abs(num)

        sign = 1
        count = 0
        while num:
            num, digit = divmod(num, 10)
            if sign > 0 and digit > 0:
                count += 1
            elif sign > 0 and digit < 0:
                count += sign
            elif sign == 0 and digit > 0:
                count += sign
            sign = sign * -1
        if count > 0:
            result += count
    return result

