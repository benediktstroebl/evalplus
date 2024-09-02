

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l2 = l
    for i in range(0, len(l2)):
        if l2[i] % 3 == 0:
            l2[i] = l2[i]
            j = i + 1
            while j < len(l2):
                if l2[j] % 3 == 0:
                    l2[i] = l2[j]
                    l2[j] = l2[i]
                j += 1
    return l2
