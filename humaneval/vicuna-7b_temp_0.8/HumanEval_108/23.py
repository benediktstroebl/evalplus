
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
    def count_digits(x):
        """
        Returns a tuple of (sum, digits) where digits is a list of digits of x,
        and sum is the sum of digits.
        """
        return sum(int(d) for d in str(x)), [int(d) for d in str(x)]

    def count_pos_digits(x):
        """
        Returns a tuple of (sum, digits) where digits is a list of digits of x,
        and sum is the sum of digits, positive digits only.
        """
        return sum(int(d) if d.isdigit() else 0 for d in str(x)), [int(d) if d.isdigit() else 0 for d in str(x)]

    def count_neg_digits(x):
        """
        Returns a tuple of (sum, digits) where digits is a list of digits of x,
        and sum is the sum of digits, negative digits only.
        """
        return sum(int(d) if d.isdigit() and d <= 0 else 0 for d in str(x)), [int(d) if d.isdigit() and d <= 0 else 0 for d in str(x)]

    def count_nums_impl(arr):
        """
        Returns the number of elements in arr with a sum of digits > 0.
        """
        return sum(count_digits(x) for x in arr)

    return count_nums_impl