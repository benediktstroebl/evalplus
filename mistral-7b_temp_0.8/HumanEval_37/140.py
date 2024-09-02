

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    def sort_even_helper(l, even_indicies):
        """A helper function to do the work.
        l is a list, and even_indicies is a list of the even indicies of l.
        Returns a list identical to l in the odd indicies, while its values at the even indicies are equal
        to the values of the even indicies of l, but sorted.
        """
        if len(even_indicies) == 0:
            return l
        even_indicies_copy = even_indicies.copy()
        even_indicies_copy[0] -= 1  # To find the first even index
        return l[:even_indicies[0]] + sort_even_helper(l[even_indicies[0]:even_indicies[0] + 2], even_indicies[1:]) + l[even_indicies[0] + 2:]
    l = l.copy()
    return sort_even_helper(l, [i for i in range(len(l)) if i % 2 == 0])
