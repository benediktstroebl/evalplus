

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    temp_even = []
    temp_odd = []
    for i in range(len(l)):
        if i % 2 == 0:
            temp_even.append(l[i])
        else:
            temp_odd.append(l[i])
    temp_even.sort()
    l = []
    for i in range(len(temp_even)):
        l.append(temp_even[i])
    for i in range(len(temp_odd)):
        l.append(temp_odd[i])
    return l

