
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
    n = len(arr)
    result = 0
    for i in range(n):
        sum = 0
        for j in range(i):
            digit = arr[j]
            sum += abs(digit) if digit >= 0 else abs(digit) * 10 + (digit % 10)
        result += sum
    return result
