

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    sorted_list = l
    for i in range(0, len(sorted_list), 2):
        if i == 0:
            continue
        else:
            sorted_list[i], sorted_list[i - 1] = sorted_list[i - 1], sorted_list[i]
    return sorted_list
