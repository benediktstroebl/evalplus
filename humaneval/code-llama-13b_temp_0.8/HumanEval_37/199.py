

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
    if n == 0:
        return []
    if n == 1:
        return l
    even_sorted = sort_even(l[1:])
    if n % 2 == 0:
        return [l[0]] + even_sorted
    return [l[0], l[2]] + even_sorted

