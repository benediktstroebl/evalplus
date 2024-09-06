

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    # first we will create a new list, even_values, which contains the even values of the original list, l.
    even_values = []
    for i in range(len(l)):
        if i % 2 == 0:
            even_values.append(l[i])
    # next we will sort the list, even_values
    even_values.sort()
    # now we will create our new list, l', and copy in the values of l
    l_prime = l.copy()
    # then we will copy the even values into l', replacing the even indicies of l' with the values of the sorted even values
    for i in range(len(even_values)):
        l_prime[2*i] = even_values[i]
    # finally, we return l'
    return l_prime



