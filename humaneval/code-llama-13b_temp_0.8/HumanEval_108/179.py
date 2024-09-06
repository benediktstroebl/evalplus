
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
    for i in range(len(arr)):
        total = 0
        num = arr[i]
        if num < 0:
            num *= -1
        while num > 0:
            total += num % 10
            num = num // 10
        if total > 0:
            nums += 1
    return nums
