
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
    def count_sign(x):
        """
        A helper function that returns -1 if x is negative, 1 if x is positive,
        and 0 if x is zero.
        """
        if x < 0:
            return -1
        elif x > 0:
            return 1
        else:
            return 0
    
    def count_sums(x):
        """
        A helper function that returns the sum of the digits of the number x.
        """
        return sum(int(d) for d in str(x))
    
    def count_nums_helper(arr, x):
        """
        Recursive function that counts the number of elements with a sum of digits > 0.
        """
        if not x:
            return 0
        if x % 10 == 0:
            return 1
        elif x < 0:
            return 1 + count_sign(abs(x))
        else:
            count = count_sign(x / 10)
            count += count_nums_helper(arr, x % 10)
            return count
    
    return count_nums_helper(arr, x)