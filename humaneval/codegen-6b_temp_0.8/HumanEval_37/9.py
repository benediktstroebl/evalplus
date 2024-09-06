

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # New list starts at index 1
    # even_l = l[0::2]
    # even_l.sort()
    # l[1::2] = even_l
    # return l
    
    # Without the above, we just need to create even and odd lists
    new_list = []
    for index in range(0, len(l), 2):
        new_list.append(l[index])
    even_list = new_list[::2]
    new_list[::2] = sorted(even_list)
    return new_list
