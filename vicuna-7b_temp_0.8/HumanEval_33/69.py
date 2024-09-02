

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = list(l)
    n = len(l)
    l_i = [l[i] for i in range(n//3)]
    l_divisible = [0] * 3
    for i in range(n):
        if i % 3 == 0:
            l_divisible += [l_i[i//3]]
    l_divisible.sort()
    l_i.extend(l_divisible)
    return l_i
