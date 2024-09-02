

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    """
    in other words, it's the same list, but with the even
    indicies sorted.
    """
    l1 = []
    for i in range(len(l)):
        if i % 2 == 0:
            l1.append(min(l[i], l[i + 1]))
        else:
            l1.append(l[i])
    return l1

