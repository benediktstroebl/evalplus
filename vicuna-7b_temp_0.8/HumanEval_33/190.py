

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    third_indices = [i for i in range(len(l)) if divmod(i, 3) == 0]
    l_sorted_by_third = sorted(l[i:i+3] for i in third_indices)
    l_sorted_by_third = sorted(l_sorted_by_third, key=lambda x: l[x//3][x%3])
    return l[third_indices] + l_sorted_by_third
