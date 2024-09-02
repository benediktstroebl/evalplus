

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even = l[0::2]
    odd = l[1::2]
    even.sort()
    l = []
    for x in range(len(even) + len(odd)):
        if x % 2 == 0:
            l.append(even[x // 2])
        else:
            l.append(odd[x // 2])
    return l

