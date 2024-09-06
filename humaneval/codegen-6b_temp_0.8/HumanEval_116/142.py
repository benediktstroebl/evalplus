
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
    b_ans = []
    d_ans = []
    for val in arr:
        b_val = bin(val)[2:]
        b_ans.append(b_val.count('1'))
        d_ans.append(val)

    index = b_ans.index(max(b_ans))
    return d_ans[:index + 1] + sorted(d_ans[index + 1:])

