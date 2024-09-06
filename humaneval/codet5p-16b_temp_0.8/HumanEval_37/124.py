

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    if len(l) == 0:
        return []

    new_list = [0] * len(l)

    current_index = 0
    current_val = l[0]
    while current_index < len(l):
        if current_val % 2 == 0:
            new_list[current_index] = current_val
        else:
            new_list[current_index] = l[current_val]
        current_index += 1

    return new_list
