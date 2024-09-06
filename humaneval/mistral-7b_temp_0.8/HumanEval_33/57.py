

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_copy = l[:]
    l_prime = []
    index = 0
    while index < len(l):
        if index % 3 != 0:
            l_prime.append(l_copy[index])
        else:
            l_prime.append(sorted(l_copy[index:index+3]))
        index += 1
    return l_prime

