

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_prime = list()
    for i in range(0, len(l)):
        if i % 3 != 0:
            l_prime.append(l[i])
        else:
            if i + 1 < len(l) and l[i] > l[i + 1]:
                l_prime.append(l[i + 1])
            else:
                l_prime.append(l[i])

    return l_prime

