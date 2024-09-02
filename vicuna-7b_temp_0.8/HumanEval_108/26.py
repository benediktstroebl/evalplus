
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
    arr = list(arr)
    n = len(arr)
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    elif n % 2 != 0:
        return arr[0] + arr[1]
    else:
        sum = 0
        for i in range(2, n):
            digit = arr[i-1] * 10 + arr[i]
            if digit > 0:
                sum += digit
        return sum
