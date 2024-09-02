

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    
    assert len(l) >= 1 and type(l[0]) == int, "list must contain integers"
    
    l_copy = l.copy()
    l_copy.sort()
    
    even_vals = []
    odd_vals = []
    
    for i in range(len(l_copy)):
        if i % 2 == 0:
            even_vals.append(l_copy[i])
        else:
            odd_vals.append(l_copy[i])
    
    return odd_vals + even_vals
    
