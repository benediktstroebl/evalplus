

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    l_2 = []
    for i in range(0, len(l)):
        if i % 2 == 0:
            l_2.append(l[i])
    l_2.sort()
    print(l_2)
    for i in range(0, len(l)):
        if i % 2 == 0:
            l[i] = l_2.pop(0)
    return l
