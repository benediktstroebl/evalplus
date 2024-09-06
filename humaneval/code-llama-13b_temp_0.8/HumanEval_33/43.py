

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    import bisect
    if not l:
        return l
    else:
        # Divide the list in two
        odds = [i for i in l if not i % 3 == 0]
        evens = [i for i in l if i % 3 == 0]
        evens.sort()
        # Merge them together
        merged = [i for i in odds]
        for i in evens:
            bisect.insort(merged, i)
        return merged



