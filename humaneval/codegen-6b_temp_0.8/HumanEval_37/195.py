

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Note: We'll assume that the input list is non-empty. Your code should't work if it
    # is not.
    
    odd = []
    even = []
    for item in l:
        if item % 2:
            odd.append(item)
        else:
            even.append(item)
    return even + sorted(odd)

