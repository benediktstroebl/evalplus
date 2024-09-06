

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
    if len(l) == 1:
        return l
    if len(l) == 2:
        if l[0] % 2 == 0:
            return l
        else:
            return [l[1], l[0]]
    elif len(l) == 3:
        if l[0] % 2 == 0:
            if l[2] % 2 == 0:
                return l
            else:
                return [l[0], l[2], l[1]]
        else:
            if l[2] % 2 == 0:
                return [l[2], l[1], l[0]]
            else:
                return [l[1], l[2], l[0]]
    l_prime = []
    i = 0
    j = 0
    while i < len(l):
        while j < len(l):
            if (l[j] % 2 == 0) and (l[j] < l[i]):
                if j == len(l)-1:
                    l_prime.append(l[i])
                else:
                    l_prime.append(l[i])
                i = j
                break
            j += 1
        if j == len(l):
            l_prime.append(l[i])
            i += 1
            j = 0
    return l_prime


