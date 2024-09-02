

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
    for i in range(0, n, 2):
        left = i
        right = i + 1
        while right < n and (l[right] % 2 == 0) and l[left] < l[right]:
            l[left], l[right] = l[right], l[left]
            left += 2
            right += 2
    return l

