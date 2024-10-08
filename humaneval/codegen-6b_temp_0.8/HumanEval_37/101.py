

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if l == []:
        return l
    else:
        sorted_list = []
        sorted_list.append(l[0])
        for i in range(1, len(l)):
            if l[i] % 2 == 0:
                sorted_list.append(l[i])
            else:
                sorted_list.append(l[i])
        return sorted_list
