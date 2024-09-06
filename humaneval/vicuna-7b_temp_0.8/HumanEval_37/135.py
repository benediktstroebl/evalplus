

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
    i = j = 0
    while i < n:
        if i + 1 < n:
            if l[i] <= l[i + 1]:
                j = i + 1
                while l[j] >= l[j - 1]:
                    j -= 1
                l[i:j + 1] = l[i:j]
        else:
            j = i + 1
            while l[j] >= l[j - 1]:
                j -= 1
                l[i] = l[j]
        i = j + 1
    return l
