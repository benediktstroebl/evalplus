

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
    for i in range(n//2):
        j = i + 1
        while j < n and l[i] < l[j]:
            l[i], l[j] = l[j], l[i]
            i += 1
            j += 1
    return l
