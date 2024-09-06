

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if len(l) == 0:
        return l
    else:
        current = l[0]
        if current % 2 == 0:
            smaller = [x for x in l[1:] if x <= current and x % 2 == 0]
            larger = [x for x in l[1:] if x > current and x % 2 == 0]
            return sort_even(smaller) + [current] + sort_even(larger)
        else:
            return [current] + sort_even(l[1:])

