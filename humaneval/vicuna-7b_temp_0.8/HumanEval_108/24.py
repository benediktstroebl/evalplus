
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
    dp = [[0] * 10 for _ in range(10)]  # 10 possible digits
    for i in range(1, len(arr)):
        dp[arr[i] // 10][(arr[i] % 10) // 10] += 1
    return sum(dp)