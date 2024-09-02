

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    list_length = len(l)
    if list_length == 0:
        return l
    else:
        even_sorted = sorted([l[i] for i in range(0, list_length, 2)])
        new_list = list(zip(even_sorted, [l[i] for i in range(1, list_length, 2)]))
        new_list = [new_list[i][0] for i in range(0, list_length, 2)] + [new_list[i][1] for i in range(0, list_length, 2)]
        return new_list

