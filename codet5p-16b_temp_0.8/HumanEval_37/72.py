

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    assert l, "empty list"
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_vals = [l[i] for i in even_indices]
    odd_vals = [l[i] for i in range(len(l)) if i % 2 == 1]
    odd_vals.sort()
    sorted_even_vals = even_vals + odd_vals
    return [sorted_even_vals[i] for i in range(len(sorted_even_vals))]
