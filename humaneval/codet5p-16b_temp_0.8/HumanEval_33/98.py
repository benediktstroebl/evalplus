

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    def sort_third_helper(l: list, index: int) -> list:
        if index >= len(l):
            return []
        elif index % 3 == 0:
            return sort_third_helper(l, index + 1) + [l[index]] + sort_third_helper(l, index + 1)
        else:
            return [l[index]] + sort_third_helper(l, index + 1)

    return sort_third_helper(l, 0)
