

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    assert l, "Input must be a non-empty list!"

    # Using this function is trivial. If there's a more efficient way, let me know.
    return [i for i in l if i % 3!= 0] + sorted([i for i in l if i % 3 == 0], reverse=True)
