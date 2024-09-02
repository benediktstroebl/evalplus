

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l2 = [None for x in range(len(l))]
    even = [x for x in range(0, len(l), 2)]
    odd = [x for x in range(1, len(l), 2)]
    for index in even:
        l2[index] = l[index]
    for index in odd:
        l2[index] = l[index]
    return l2
