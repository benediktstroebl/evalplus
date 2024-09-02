

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_idx = []
    odd_idx = []
    for idx, val in enumerate(l):
        if idx % 2 == 0:
            even_idx.append(idx)
        else:
            odd_idx.append(idx)
    l' = [l[idx] for idx in odd_idx]
    for i in even_idx:
        l'[i] = sorted(l[i:i + 2])[0]
    return l'

