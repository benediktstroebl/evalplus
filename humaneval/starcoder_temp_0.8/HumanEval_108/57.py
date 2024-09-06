
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
    # base case
    if len(arr) == 0:
        return 0

    # recursive case
    sum_nums = 0
    for i in arr:
        if sum_nums > 0:
            if i < 0:
                i = i * -1
                sum_nums += i
            else:
                sum_nums += i
        elif sum_nums <= 0:
            if i > 0:
                sum_nums += i
            else:
                sum_nums += i * -1
    return count_nums(arr[1:]) + 1 if sum_nums > 0 else count_nums(arr[1:])

