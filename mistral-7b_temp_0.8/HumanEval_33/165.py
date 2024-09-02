

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_len = len(l)
    l_ind = 0
    l_prime = []
    while l_len > 0:
        if l_ind % 3 != 0:
            l_prime.append(l[l_ind])
        else:
            l_prime.append(sorted(l)[l_ind])
        l_ind += 1
        l_len -= 1
    return l_prime

