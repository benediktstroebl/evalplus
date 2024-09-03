def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    Test suite:
    >>> sorted(list_to_test()) == [0, 2, 4, 6, 8, 10]
    True
    """
    l_copy = list(l)
    l_copy.remove(3)
    l_copy[::3] = l_copy[::3] + l_copy[::3+1]
    return l_copy