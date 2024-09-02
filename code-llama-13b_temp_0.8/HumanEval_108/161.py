
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

    num_sum_gt_0 = 0
    for num in arr:
        num_sum = 0
        while num != 0:
            if num < 0:
                num_sum += num % 10
                num = num // 10
            else:
                num_sum += num % 10
                num = num // 10
        if num_sum > 0:
            num_sum_gt_0 += 1
    return num_sum_gt_0
