

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
        return []
    else:
        sorted_tail = sort_even(l[1:])
        if len(l) == 1:
            return l
        else:
            if l[0] % 2 == 0:
                if l[0] > sorted_tail[0]:
                    sorted_tail[0] = l[0]
                if l[0] < sorted_tail[-1]:
                    sorted_tail[-1] = l[0]
                return sorted_tail
            else:
                return [l[0]] + sorted_tail



