

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    
    even_indicies = []
    even_values = []
    
    for idx in range(len(l)):
        if idx % 2 == 0:
            even_indicies.append(idx)
            even_values.append(l[idx])
    
    even_values.sort()
    
    for idx in range(len(l)):
        if idx % 2 == 0:
            l[idx] = even_values[even_indicies.index(idx)]
    
    return l
