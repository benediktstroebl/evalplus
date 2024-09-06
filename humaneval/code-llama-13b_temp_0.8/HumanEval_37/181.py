

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if len(l) == 0:
        return l
    else:
        even_sorted = sort_even(l[2:])
        if len(l) == 1:
            return l + even_sorted
        if l[0] % 2 == 0 and l[1] % 2 == 0:
            if l[0] > l[1]:
                return l[:1] + even_sorted
            else:
                return [l[1]] + l[:1] + even_sorted
        if l[0] % 2 == 0 and l[1] % 2 == 1:
            return [l[0]] + l[2:] + [l[1]] + even_sorted
        if l[0] % 2 == 1 and l[1] % 2 == 0:
            if l[0] > l[2]:
                return l[:1] + even_sorted + [l[1]]
            else:
                return [l[0]] + even_sorted + [l[1]]
        if l[0] % 2 == 1 and l[1] % 2 == 1:
            if l[0] > l[2]:
                return [l[2], l[0], l[1]] + even_sorted
            else:
                return l[:1] + even_sorted + [l[1]]




























































































































































































