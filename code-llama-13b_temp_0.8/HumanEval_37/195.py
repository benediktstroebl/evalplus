

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    a = l.copy()
    n = len(a)
    if n > 1:
        even_sort = []
        for i in range(0, n, 2):
            even_sort.append(a[i])
        even_sort.sort()
        for i in range(0, n, 2):
            a[i] = even_sort[i // 2]
    return a

