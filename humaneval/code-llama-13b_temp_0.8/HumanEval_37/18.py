

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    even_idx = []
    odd_idx = []
    for i in range(len(l)):
        if i % 2 == 0:
            even_idx.append(i)
        else:
            odd_idx.append(i)
    # get the even indicies in a list
    even_idx = [even_idx[i] for i in range(len(even_idx))]
    # get the odd indicies in a list
    odd_idx = [odd_idx[i] for i in range(len(odd_idx))]
    # copy the list
    l_copy = [l[i] for i in range(len(l))]
    # for each even index, swap the value in even index with the value in the same index in l_copy
    for i in even_idx:
        l_copy[i] = l[i]
    # sort the list
    l_copy.sort()
    # for each even index, swap the value in even index with the value in the same index in l_copy
    for i in even_idx:
        l[i] = l_copy[i]
    # for each odd index, swap the value in even index with the value in the same index in l_copy
    for i in odd_idx:
        l[i] = l_copy[i]
    return l

