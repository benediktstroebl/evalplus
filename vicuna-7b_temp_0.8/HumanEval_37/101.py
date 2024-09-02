

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
    l_even = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            l_even[i][j] = l[i][j]
    for i in range(n):
        for j in range(i+1, n):
            if l[i][j] > l_even[i][j]:
                l_even[i][j] = l[i][j]
    return l_even
