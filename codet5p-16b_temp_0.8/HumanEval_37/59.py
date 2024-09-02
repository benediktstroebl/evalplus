

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    l_copy = l[:]
    even_index = len(l_copy)-1
    odd_index = 0
    while even_index >= 0:
        if even_index % 2 == 0:
            l_copy[odd_index] = l_copy[even_index]
            odd_index += 1
            even_index -= 1
        else:
            even_index -= 1
    return l_copy

