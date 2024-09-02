

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if len(l) <= 1:
        return l
    even_values = []
    for i in range(1, len(l)):
        if i % 2 == 0:
            even_values.append(l[i])

    even_values.sort()

    l_prime = l.copy()
    j = 0
    for i in range(1, len(l_prime)):
        if i % 2 == 0:
            l_prime[i] = even_values[j]
            j += 1
    return l_prime

