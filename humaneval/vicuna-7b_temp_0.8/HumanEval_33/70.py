

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    size = len(l)
    left = size // 3
    if size % 3 == 0:
        right = size // 3 + 1
    else:
        right = size // 3
    l_third = l[left:right]
    l_third.sort(key=lambda x: x // 3)
    l_third.reverse()
    l_third.append(l[left % 3])
    return l_third