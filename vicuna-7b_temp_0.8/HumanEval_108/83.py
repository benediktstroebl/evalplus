
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
    if not arr:
        return 0
    sum = 0
    for num in arr:
        sign = 0
        num = abs(num)
        if num > 0:
            num = num - 1
            sum += num
        elif num < 0:
            sum += num * -1
        else:
            return 0
    return sum
