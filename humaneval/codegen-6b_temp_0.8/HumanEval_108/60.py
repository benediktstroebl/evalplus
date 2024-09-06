
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

    nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    curr_sum = 0
    count = 0

    for num in arr:
        str_num = str(num)
        curr_sum = 0
        for n in str_num:
            curr_sum += int(n)

        if curr_sum in nums:
            count += 1

    return count

