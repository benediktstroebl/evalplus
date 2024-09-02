
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
    def count_sign_digits(num):
        """
        Recursive function to count the number of positive digits in a number
        """
        if num == 0:
            return 1
        elif num % 10 == 0:
            return 1 + count_sign_digits(num // 10)
        else:
            return 1 + count_sign_digits(num - 1)

    def count_pos_digits(arr):
        """
        Recursive function to count the number of positive digits in an array
        """
        if not arr:
            return 0
        return sum(count_sign_digits(arr[0]) for arr in arr[1:])

    return count_pos_digits(arr)