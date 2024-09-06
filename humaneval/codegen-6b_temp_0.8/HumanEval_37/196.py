

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    start = 0
    end = len(l) - 1
    while start < end:
        if l[start]%2 != 0:
            l[start], l[end] = l[end], l[start]
            end -= 1
        else:
            start += 1
    return l

