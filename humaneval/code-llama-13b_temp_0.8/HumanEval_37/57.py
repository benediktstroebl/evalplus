

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    if len(l) == 0:
        return l
    if len(l) == 1:
        return l
    
    odd = l[1::2]
    even = l[0::2]
    odd_sorted = sorted(odd)
    i = 0
    while i < len(even):
        l.remove(even[i])
        i += 1
    j = 0
    while j < len(odd_sorted):
        l.insert(2*j, odd_sorted[j])
        j += 1

    return l

