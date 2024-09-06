
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
    # NOTE: this is a binary search, resposes to the "binsearch" code challenge
    def count_ones(number):
        n = 0
        while number > 0:
            n += 1
            number &= number - 1
        return n

    def sort(arr):
        arr.sort(key=lambda x: (count_ones(x), x))
        return arr

    return sort(arr)
