
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
    sum = 0
    for i in range(n):
        s = sum_of_digits(arr[i])
        if s > 0:
            sum += s
            if i < n - 1:
                count_nums(arr[:i])
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return sum
