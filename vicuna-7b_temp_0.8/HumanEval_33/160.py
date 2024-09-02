

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    size = len(l)
    l_third = [[l[i::3] for i in range(size//3)] for _ in range(size//3)]
    l_sorted = [sorted(lst) for lst in l_third]
    result = []
    for i in range(size):
        for j in range(size//3):
            result.append(l_sorted[j][i])
    return result