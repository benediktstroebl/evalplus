

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    def temp_sort(l):
        """Reorder the list and return it."""
        result = []
        for i in l:
            if i % 3 == 0:
                result.append(i)
        for i in l:
            if i % 3 == 1:
                result.append(i)
        for i in l:
            if i % 3 == 2:
                result.append(i)
        return result
    return temp_sort(l)
