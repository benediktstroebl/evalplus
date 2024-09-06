

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    n = len(l)
    if n < 3:
        return l
    else:
        p = n % 3
        q = n // 3
        if p != 0:
            r = [l[i::q] for i in range(q)]
            for i in range(q):
                r[i].sort()
            x = [r[j][i] for i in range(p) for j in range(q)]
            y = [r[j][i] for j in range(q) for i in range(p, q)]
            return x + y
        else:
            return sort_third(l[:-q]) + l[-q:]



