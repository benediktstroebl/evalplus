

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # for the odd indices, return the original value
    l_odd = l[:]
    l_even = []
    # for the even indices, sort and merge with l_odd
    for i in range(len(l), 0, 2):
        l_even.append(l[i])
        if l[i-1] > l_odd[i-1]:
            l_odd.append(l_odd[i-1])
    return l_odd + l_even