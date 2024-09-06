

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    if l == []:
        return []
    if len(l) == 1:
        return l
    else:
        first = l[0]
        second = l[1]
        third = l[2]
        if first % 3 == 0:
            if second % 3 == 0:
                if third % 3 == 0:
                    return l
                else:
                    return [second, third, first]
            else:
                return [third, first, second]
        else:
            if second % 3 == 0:
                if third % 3 == 0:
                    return [first, third, second]
                else:
                    return [first, second, third]
            else:
                return [first, second, third]

