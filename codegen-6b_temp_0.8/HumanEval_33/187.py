

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    copy_no_third = l[:]
    l.sort(key=lambda x: x % 3)
    first_third = l[:len(l)//3]
    second_third = l[len(l)//3:2*len(l)//3]
    last_third = l[2*len(l)//3:]
    return first_third + second_third + last_third
