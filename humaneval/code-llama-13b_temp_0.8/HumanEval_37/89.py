

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
        # Base Case
        # when we're on the first index
        if len(l) == 2:
            if l[0]%2 != 0:
                if l[1] < l[0]:
                    return [l[1], l[0]]
                else:
                    return [l[0], l[1]]
            else:
                return l
        # Recursive Case
        # when we're not on the first index
        else:
            # we're only swapping with the first element, so no need to copy the list
            if l[0]%2 != 0:
                if l[1] < l[0]:
                    l[1], l[0] = l[0], l[1]
                return l + sort_even(l[2:])
            else:
                return l[:1] + sort_even(l[2:])

