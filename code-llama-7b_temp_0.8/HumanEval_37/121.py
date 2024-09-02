

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = list(range(1, len(l), 2))
    even_indices_sorted = sorted(even_indices)
    even_indices_sorted_to_even_indices = dict(zip(even_indices_sorted, even_indices))
    even_indices_sorted_to_values = dict(zip(even_indices_sorted, [l[i] for i in even_indices]))
    even_indices_sorted = [even_indices_sorted_to_even_indices[i] for i in even_indices_sorted]
    even_indices_sorted_to_even_indices = dict(zip(even_indices_sorted, even_indices))
    sorted_l = [l[i] if i % 2 == 1 else even_indices_sorted_to_values[even_indices_sorted_to_even_indices[i]] for i in range(len(l))]
    return sorted_l

