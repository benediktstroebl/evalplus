

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_sorted = []
    for x in range(len(l)):
        if x%2 == 0:
            even_sorted.append(l[x])
    for x in range(len(l)):
        if x%2 == 0:
            l[x] = even_sorted[x//2]
    return l
