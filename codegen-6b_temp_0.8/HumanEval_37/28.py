

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    assert len(l) > 0, 'list cannot be empty'
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] % 2 == 0 and l[j] > l[i]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l
