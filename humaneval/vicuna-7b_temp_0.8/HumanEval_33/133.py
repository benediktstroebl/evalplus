

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_sort = [sorted(li) for li in l]
    l_index_not_divisible_by_3 = [x[::3] for x in l_sort]
    l_index_divisible_by_3 = [x[1::3] for x in l_sort]
    l_index_not_divisible_by_3 = [x[i::3] if len(x) > 0 else x[0] for x in l_index_not_divisible_by_3]
    l_index_divisible_by_3 = [x[i::3] if len(x) > 0 else x[0] for x in l_index_divisible_by_3]
    l_sort = [x for x in l_index_not_divisible_by_3 if x != l[i] or l[i+1] != x for i in range(len(l)-1)]
    l_sort.extend(l_index_divisible_by_3)
    l_sort.extend(l_index_divisible_by_3[::-1])
    return l_sort
