

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if len(l) <= 2:
        return l
    elif len(l) == 3:
        if l[1] > l[2]:
            return [l[0], l[2], l[1]]
    elif len(l) == 4:
        if l[1] > l[3]:
            return [l[0], l[3], l[1], l[2]]
        elif l[2] > l[3]:
            return [l[0], l[2], l[3], l[1]]
    elif len(l) > 4:
        i = 0
        while i < len(l):
            if i % 2 == 0:
                if l[i] > l[i + 1]:
                    l[i], l[i + 1] = l[i + 1], l[i]
            i += 1
        return l

