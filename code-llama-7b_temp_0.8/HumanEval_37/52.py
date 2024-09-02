

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # this solution is O(n) in time and O(n) in space
    # it uses a list comprehension, so it's O(n) in space

    # preallocate a list of None of the same size as the input list
    l2 = [None]*len(l)

    # iterate over the even indicies of l
    for i in range(0, len(l), 2):
        # keep the value of the even indicies in l at l2
        l2[i] = l[i]

    # sort the list of values at the even indicies of l
    l2[1::2] = sorted(l[1::2])

    return l2
