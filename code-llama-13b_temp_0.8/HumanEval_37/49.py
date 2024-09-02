

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_index_list = []
    odd_index_list = []
    for i in range(len(l)):
        if i % 2 == 0:
            even_index_list.append(l[i])
        else:
            odd_index_list.append(l[i])
    sorted_even_index_list = sorted(even_index_list)
    sorted_list = []
    for i in range(len(l)):
        if i % 2 == 0:
            sorted_list.append(sorted_even_index_list.pop(0))
        else:
            sorted_list.append(odd_index_list.pop(0))
    return sorted_list



