
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
    lst = []
    lst1 = []
    for i in arr:
        lst.append(bin(i))
    for j in lst:
        if j == "0b0":
            lst1.append(j)
    for k in lst:
        if k not in lst1:
            lst1.append(k)
    for m in lst1:
        if m[2:] == "":
            lst1.remove(m)
    lst1 = list(sorted(lst1))
    lst2 = []
    for n in arr:
        for o in lst1:
            if o[2:] == bin(n)[2:]:
                lst2.append(n)
    return lst2

