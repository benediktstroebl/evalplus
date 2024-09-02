

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    """ 
    -- start by copying the list so that we can have two pointers and
    -- preserve the original.
    -- since we have two pointers and the original, we can save some space 
    -- by overwriting the original.
    -- we can sort the list in place by using two pointers
    -- even pointer and odd pointer.
    -- swap if needed.
    -- increment the pointers until the pointers cross.
    -- return the result.
    """
    # l2 = l.copy()
    # i, j = 0, 1
    # while i < j:
    #     if l2[i] > l2[j]:
    #         l2[i], l2[j] = l2[j], l2[i]
    #     if j < len(l2) - 1:
    #         j += 2
    #     if i < len(l2) - 1:
    #         i += 2
    # return l2
    return sorted(l[::2]) + l[1::2]
