
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
    else:
        n = arr[0]
        count = 0
        if n > 0:
            while n!= 0:
                r = n % 10
                count += r
                n = n // 10
        else:
            while n!= 0:
                r = n % 10
                count += r
                n = -(n // 10)
        if count > 0:
            return count_nums(arr[1:]) + 1
        else:
            return count_nums(arr[1:])

