

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    length = len(l)
    for i in range(0, length, 3):
        for j in range(i, length, 3):
            if j+1 < length and l[j+1] < l[j]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
            if j+2 < length and l[j+2] < l[j]:
                temp = l[j]
                l[j] = l[j+2]
                l[j+2] = temp
    return l
