

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Even and Odd indicies
    n = len(l)
    even = l[:n//2]
    odd = l[n//2:]
    
    # sort even indicies
    even_sorted = sorted(even)
    even = [x for x in even if x not in [0, 1]]
    
    # sort odd indicies
    odd_sorted = sorted(odd)
    odd = [x for x in odd if x not in [0, 1]]
    
    # concatenate the sorted even and odd lists
    l_sorted = even + odd
    
    return l_sorted
