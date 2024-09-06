

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l.sort()
    return l

a = [1, 2, 3]
b = [5, 6, 3, 4, 8, 9, 2]
c = sort_third(b)
assert c == [2, 6, 3, 4, 8, 9, 5]
assert a == [1, 2, 3]
assert b == [5, 6, 3, 4, 8, 9, 2]