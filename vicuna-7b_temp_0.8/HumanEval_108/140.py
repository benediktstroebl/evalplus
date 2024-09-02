
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
        Helper function to count the number of negative and positive signed digits in a number
        """
        return sum(map(int, [x if x < 0 else abs(x) for x in num]))

    def count_digits(num):
        """
        Helper function to count the number of digits in a number
        """
        return len(str(num))

    return max(count_signed_digits(arr[0]), count_digits(arr[0]))
