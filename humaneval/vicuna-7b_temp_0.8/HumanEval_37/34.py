

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    n = len(l)
    i = 0
    l_even = [x for x in l[i:n] if x % 2 == 0]
    i = n
    while i > 0:
        l_even.append((l[i-1] if i-1 >= 0 else 0) + (l_even[i] if i < len(l_even) else 0))
        i -= 2
    return l_even