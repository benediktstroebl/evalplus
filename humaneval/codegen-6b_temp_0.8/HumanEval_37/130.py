

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    
    l1 = l.copy()
    even_index = 0
    for i in l:
        if i % 2 == 0:
            l1[even_index] = i
            even_index += 1
            l1[even_index] = i
        else:
            l1[even_index] = i
            even_index += 1
    return l1
