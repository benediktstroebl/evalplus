

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    n = len(l)
    if n <= 1:
        return l
    # 根据偶数位和奇数位分别排序
    even = l[::2]
    odd = l[1::2]
    even.sort()
    odd.sort()
    # 将排序后的偶数位和奇数位合并
    l = [val for pair in zip(even, odd) for val in pair]
    return l
