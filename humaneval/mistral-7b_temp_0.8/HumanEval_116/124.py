
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
    #code
    def bin_rep(n):
        return bin(n).replace("0b","")
    a = []
    b = []
    for i in arr:
        a.append(bin_rep(i))
        b.append(int(i))
    return sorted(a, key=b.__getitem__)

















































































































































































