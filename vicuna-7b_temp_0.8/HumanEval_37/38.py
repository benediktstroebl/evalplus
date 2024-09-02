

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
    l_mod = l[:n//2]  # l in odd indices
    l_even = l[n//2]  # l in even indices
    
    l_mod.sort()
    l_even.sort()
    
    return [l_mod[i] if i % 2 == 0 else l_even[i] for i in range(n)]