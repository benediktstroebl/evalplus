

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if not l:
        return l
    if len(l) == 1:
        return l
    odd_part = l[1::2]
    even_part = l[::2]
    if not odd_part:
        return l
    if len(odd_part) == 1:
        return l
    sorted_odd = sort_even(odd_part)
    sorted_even = sorted(even_part)
    l_prime = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_prime.append(sorted_even[i//2])
        else:
            l_prime.append(sorted_odd[i//2])
    return l_prime

