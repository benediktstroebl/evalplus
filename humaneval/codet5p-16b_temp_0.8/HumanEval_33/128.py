

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    indices = [i for i in range(len(l))]
    indices_3 = [i for i in range(len(l)) if i % 3 == 0]
    sorted_indices_3 = sorted(indices_3)
    sorted_indices = sorted(indices)
    
    result = [None for _ in range(len(l))]
    result_3 = [None for _ in range(len(l))]
    
    for i in range(len(l)):
        if i not in sorted_indices_3:
            result[i] = l[i]
        else:
            result_3[i] = l[i]
    for i in range(len(result_3)):
        result[sorted_indices_3[i]] = result_3[i]
    return result
