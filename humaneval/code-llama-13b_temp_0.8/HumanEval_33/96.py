

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    if len(l) < 3:
        return l
    else:
        head = l[0]
        tail = l[1:]
        tail_sorted = sort_third(tail)
        head_sorted = l[2]
        if head_sorted < head:
            return [head_sorted, tail_sorted[0], tail_sorted[1]] + tail_sorted[2:]
        else:
            return [head, tail_sorted[0], tail_sorted[1]] + tail_sorted[2:]
    
