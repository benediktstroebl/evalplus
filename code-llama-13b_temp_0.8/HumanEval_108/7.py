
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
    nums = 0
    for n in arr:
        if n >= 0:
            sum_of_digits = 0
            while n != 0:
                sum_of_digits += n % 10
                n = n // 10
        else:
            sum_of_digits = -n % 10
            n = n // 10
            while n != 0:
                sum_of_digits += n % 10
                n = n // 10
        if sum_of_digits > 0:
            nums += 1
    return nums
