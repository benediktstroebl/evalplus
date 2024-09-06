

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    """BEGIN PROBLEM 1.2"""
    sorted_list = l[:]
    odd = sorted_list[::2]
    even = sorted_list[1::2]
    sorted_odd = sorted(odd)
    sorted_even = sorted(even)
    sorted_list[::2] = sorted_odd
    sorted_list[1::2] = sorted_even
    return sorted_list
    """END PROBLEM 1.2"""
