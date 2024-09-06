

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
    elif len(l) == 1:
        return l
    else:
        even_l = l[0::2]
        odd_l = l[1::2]

        if even_l == []:
            return odd_l
        elif even_l == [[]]:
            return l
        else:
            even_l.sort()
            l_new = []
            l_new += even_l
            l_new += odd_l
            return l_new
