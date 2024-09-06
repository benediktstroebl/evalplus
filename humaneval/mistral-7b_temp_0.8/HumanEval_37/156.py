

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    def _sort_even(l: list, n: int):
        """Sorts the even indicies of the list l up to (and including) the nth index.
        >>> _sort_even([5, 3, 4, 6], 1)
        [5, 3, 4, 6]
        >>> _sort_even([5, 3, 4, 6], 2)
        [5, 3, 4, 6]
        >>> _sort_even([5, 3, 4, 6], 3)
        [3, 5, 4, 6]
        """

        if n == 0:
            return

        _sort_even(l, n - 1)
        temp = l[n]
        l[n] = l[n - 1]
        l[n - 1] = temp
        return l

    l_sorted = [0] * len(l)
    for i in range(0, len(l)):
        if i % 2 != 0:
