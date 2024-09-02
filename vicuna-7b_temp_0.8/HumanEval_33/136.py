

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    low = 0
    high = len(l) - 1
    while low <= high:
        index = (low + high) // 2
        if (l[index] % 3 == 0) == l[index]:
            l[low:high+1] = l[index:index+1]
            low = index + 1
        else:
            low = index + 1
        high = (low + high) // 2
    return l
