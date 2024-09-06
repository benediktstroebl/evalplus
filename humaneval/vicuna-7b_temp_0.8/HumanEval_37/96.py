

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    n = len(l)
    i, j = 0, n // 2
    lj = [l[i] for i in range(n)]
    while i < j:
        if lj[i] <= l[j]:
            # sort even indicies
            lj_ = []
            for k in range(i, n):
                lj_ += [l[k] if l[k] <= l[j] else lj[k-1]]
            lj = lj_
            i += 1
        else:
            # swap elements
            lj[i], lj[j] = lj[j], lj[i]
            i += 1
            j -= 1
    return lj
