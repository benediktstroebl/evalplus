

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l = list(l)
    i = 0
    while i < len(l) - 1:
        if l[i] % 2 == 0:
            # for even number, swap with the next even number
            j = i + 1
            while j < len(l) and l[j] % 2 == 0:
                l[i], l[j] = l[j], l[i]
                i += 1
                j += 1
        else:
            # for odd number, swap with the next odd number
            j = i + 1
            while j < len(l) and l[j] % 2 != 0:
                l[i], l[j] = l[j], l[i]
                i += 1
                j += 1
    return l
