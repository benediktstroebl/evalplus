
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

    for x in arr:
        if x > 0:
            sum_of_digits = 0
            while x > 0:
                digit = x % 10
                sum_of_digits += digit
                x //= 10
            if sum_of_digits > 0:
                count += 1
        elif x < 0:
            sum_of_digits = 0
            while x != 0:
                digit = x % 10
                sum_of_digits += digit
                x //= 10
            if sum_of_digits > 0:
                count += 1
        else:
            count += 1

    return count
