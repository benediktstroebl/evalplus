
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
    def count_signed_digits(num):
        """
        Count the number of negative and positive signed digits in the number.
        """
        if num < 0:
            return 0, 1
        else:
            return 0, 0
    count = 0
    count_signed = 0
    for i in arr:
        count, count_signed = count_signed_digits(i)
        count += count_signed
    return count
