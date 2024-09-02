

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # the even indicies are all at indices 2, 4, 6, etc.
    # the odd indicies are all at indices 1, 3, 5, etc.


    for i in range(1, int(len(l) / 2)):
        left = 2 * i - 1
        right = 2 * i
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left]

    return l
