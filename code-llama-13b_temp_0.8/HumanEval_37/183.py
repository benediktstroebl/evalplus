

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    # Base case
    if len(l) == 0:
        return l

    # Inductive step
    else:
        first = l[0]
        # Check to see if the first element is even
        if first % 2 == 0:
            first_even = True
        else:
            first_even = False

        # Split l into two lists, l_even and l_odd
        l_even = []
        l_odd = []
        for x in l:
            if x % 2 == 0:
                l_even.append(x)
            else:
                l_odd.append(x)

        # Sort l_even
        l_even.sort()

        # Merge l_even and l_odd back into a single list, l'
        if first_even:
            l_prime = l_even
            l_prime.insert(0, l_odd[0])
            l_prime.extend(l_odd[1:])
        else:
            l_prime = l_odd
            l_prime.insert(0, l_even[0])
            l_prime.extend(l_even[1:])

        return l_prime










