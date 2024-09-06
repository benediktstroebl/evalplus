

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    for i in range(len(l)):
        if i % 2 == 0:
            # Even index
            val = l[i]
            min_val = val
            min_index = i
            for j in range(i, len(l), 2):
                if l[j] < min_val:
                    min_val = l[j]
                    min_index = j
            l[min_index] = val
            l[i] = min_val
    return l
