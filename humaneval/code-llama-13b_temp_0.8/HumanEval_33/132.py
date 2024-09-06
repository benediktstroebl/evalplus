

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # def sort_third_helper(l, start):
    #     if start >= len(l) - 1:
    #         return l
    #     if start % 3 == 0:
    #         l[start: start + 3] = sorted(l[start: start + 3])
    #     sort_third_helper(l, start + 1)
    #     return l
    # return sort_third_helper(l, 0)
    out = []
    for i in range(len(l)):
        if i % 3 == 0:
            out += sorted(l[i:i+3])
        else:
            out += [l[i]]
    return out

