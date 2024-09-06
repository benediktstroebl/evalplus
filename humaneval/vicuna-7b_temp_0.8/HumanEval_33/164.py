

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    if len(l) <= 1:
        return l
    n = len(l)
    l_third = [l[i] for i in range(n//3) if i < n]
    l_third.sort()
    l_third.extend([l[i] for i in range(n//3) if i == n//3])
    l_third.extend(l[i] for i in range(n//3) if i + n//3 < n)
    l = [0] * n
    for i in l_third:
        l[i // 3] = i
    return l