

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l = list(l)
    l_copy = list(l)
    l_copy.sort()
    l_copy_odd = []
    l_copy_even = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_copy_even.append(l_copy[i])
        else:
            l_copy_odd.append(l_copy[i])
    l_new = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_new.append(l_copy_even[i])
        else:
            l_new.append(l_copy_odd[i])
    return l_new

