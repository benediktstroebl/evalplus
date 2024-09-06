
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    from operator import itemgetter

    def get_ones_count(n):
        c = 0
        while n:
            c += n % 2
            n //= 2
        return c

    res = sorted(enumerate(arr), key=itemgetter(1, 0))
    return [x[1] for x in res]
