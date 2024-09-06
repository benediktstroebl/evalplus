

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    new_list = []
    even = []
    odd = []
    for index, item in enumerate(l):
        if index % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    even.sort()
    new_list.append(even)
    new_list.append(odd)
    new_list = [item for sublist in new_list for item in sublist]
    return new_list

