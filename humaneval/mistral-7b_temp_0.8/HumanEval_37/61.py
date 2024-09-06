

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    l_prime = list()
    index = 0

    while index < len(l):

        if index % 2 == 0:
            # The index is even, so we need to sort the value
            l_prime.append(sorted(l[index])[0])
        else:
            # The index is odd, so we can just append the value
            l_prime.append(l[index])

        index += 1

    return l_prime

