

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_index_one = [i for i in range(len(l)) if not divmod(i, 3) in [0, 1, 2]]
    l_index_two = [i for i in range(len(l)) if divmod(i, 3) in [0, 1, 2]]
    l_index_three = [i for i in range(len(l)) if divmod(i, 3) in [0, 1]]
    l_values = l[l_index_one] + l[l_index_two] + l[l_index_three]
    l_sorted = sorted(l_values)
    return l_sorted