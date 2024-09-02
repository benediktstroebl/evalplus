

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = l[:]  # This is to preserve the original list
    i = 0
    while i < len(l) // 3:
        j = i + 2
        while j < len(l) and l[j] == l[i]:
            j += 2
        l[i:j] = l[i:j][::-1]
        i = j + 1
    return l
