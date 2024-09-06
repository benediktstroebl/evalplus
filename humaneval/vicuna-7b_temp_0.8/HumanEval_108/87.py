
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
    # Your code here
    sum_pos = 0
    for num in arr:
        sign = 0
        if num < 0:
            sign = 1
        digit = sum(map(int, [num // 10 ** i for i in range(1, 10)]))
        if digit > 0:
            sum_pos += digit
    return sum_pos
