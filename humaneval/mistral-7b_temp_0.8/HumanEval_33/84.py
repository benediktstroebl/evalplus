

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    def sort_third_helper(l, start, end):
        if start == end:
            return l[start]
        else:
            i = start + 2
            while i <= end and i % 3 == 0:
                l[i], l[i - 1] = l[i - 1], l[i]
                i += 2
            return l[start] + sort_third_helper(l, start + 1, end)

    l_sorted_third = l.copy()
    for i in range(0, len(l), 3):
        l_sorted_third[i] = sort_third_helper(l_sorted_third, i + 1, i + 2)
    return l_sorted_third

