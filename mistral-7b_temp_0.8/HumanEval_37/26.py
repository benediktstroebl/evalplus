

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_odd = []
    l_even = []

    for i in range(0, len(l)):
        if i % 2 != 0:
            l_odd.append(l[i])
        else:
            l_even.append(l[i])

    l_even.sort()

    l_sorted = []
    for i in range(0, len(l)):
        if i % 2 != 0:
            l_sorted.append(l_odd[i])
        else:
            l_sorted.append(l_even[i-1])

    return l_sorted

