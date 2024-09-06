

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l = l[:]  # 将 l 复制一下
    # 将偶数的元素按照从小到大排序
    for i in range(len(l) / 2):
        j = i + 1
        if j < len(l):
            while l[j] > l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
            l[j] = max(l[j], l[j - 1])
    return l