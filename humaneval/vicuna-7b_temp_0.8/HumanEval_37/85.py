

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
    if n < 2:
        return l
    i = 0
    j = 0
    pivot = l[n // 2]
    while i < n:
        while l[i] < pivot:
            i += 1
        while l[j] > pivot:
            j += 1
        l[i], l[j] = l[j], l[i]
        i += 1
        j += 1
    return l[j:n]
