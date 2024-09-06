

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    def helper(l, i, j):
        if i == j:
            return l[i]
        elif i % 3 == 0:
            return helper(l, i + 1, j)
        else:
            return helper(l, i + 1, j + 1)

    for i in range(len(l) // 3):
        for j in range(3):
            l[i*3 + j], l[i*3 + j + 1] = helper(l, i*3 + j, i*3 + j + 1)

    return l
