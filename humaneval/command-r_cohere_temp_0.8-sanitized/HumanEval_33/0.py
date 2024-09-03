def sort_third(l: list):
    """
    Sorts the values of the list l that lie at indicies divisible by three, while keeping the other values unchanged.

    Parameters:
        l (list): The input list.

    Returns:
        list: A new list with the values at indices divisible by three sorted, and the other values unchanged.
    """
    l_new = l.copy()
    third_indices = [i for i in range(len(l_new)) if i % 3 == 0]

    values_at_third_indices = [l_new[idx] for idx in third_indices]
    sorted_values = sorted(values_at_third_indices)

    for idx, val in enumerate(sorted_values):
        l_new[third_indices[idx]] = val

    return l_new