

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Make a copy of the list
    l = l[:]
    # Iterate over the list
    for i in range(len(l)):
        # If the current index is even, compare the values of the current element with the next one
        if i % 2 == 0:
            j = i + 1
            while j < len(l) and l[j] > l[i]:
                l[i], l[j] = l[j], l[i]
                j += 1
    return l
