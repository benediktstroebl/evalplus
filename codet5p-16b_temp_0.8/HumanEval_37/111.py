

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    evens = []
    for i in range(len(l)):
        if i % 2 == 0:
            evens.append(l[i])
    evens.sort()
    new_l = l[:]
    for i in range(len(new_l)):
        if i % 2 == 0:
            new_l[i] = evens[0]
            evens.pop(0)
    return new_l




