

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
        return l
    elif len(l) == 1:
        return l
    elif len(l) == 2:
        if l[1] > l[0]:
            return [l[0], l[1]]
        else:
            return [l[1], l[0]]
    else:
        even_list = list()
        for i in range(1, len(l)):
            if i % 2 == 0:
                even_list.append(l[i])
        even_list.sort()
        l_copy = list(l)
        for i in range(1, len(l)):
            if i % 2 == 0:
                l_copy[i] = even_list[i // 2]
        return l_copy

