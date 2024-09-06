
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
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    else:
        count = 0
        for i in range(n):
            digit = arr[i]
            count += digit if digit > 0 else digit + count * 10
        return count
