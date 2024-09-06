

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # l[0] is the first element
    # l[-1] is the last element
    # l[1:-1] is the remaining elements
    return sorted([l[0]] +  # [1]
                  [l[i] for i in xrange(1, len(l)-1) if not i % 3] +  # [2]
                  [l[-1]])  # [3]

