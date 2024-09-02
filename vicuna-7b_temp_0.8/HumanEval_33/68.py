

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    if not l:
        return l
    pivot = l[0]
    l1 = l[1:len(l)//3]
    l2 = l[len(l)//3:]
    l1 = [i for i in l1 if i <= pivot]
    l2 = [i for i in l2 if i <= pivot]
    return l1 + [pivot] + l2