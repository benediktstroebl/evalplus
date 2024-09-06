
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

    n = len(arr)
    m = []
    for i in range(n):
        num = arr[i]
        count = 0
        while num:
            if num & 1 == 1:
                count += 1
            num >>= 1
        m.append((count, i))
    m.sort()
    ans = [0] * n
    for i in range(n):
        ans[m[i][1]] = arr[i]
    return ans
