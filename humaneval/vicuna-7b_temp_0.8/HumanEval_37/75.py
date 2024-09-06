

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    low = 0
    high = len(l) // 2
    pivot = l[high]
    while low <= high:
        while l[low] < pivot:
            low += 1
        while l[high] > pivot:
            high -= 1
        if low <= high:
            l[low], l[high] = l[high], l[low]
            low += 1
            high -= 1
    return l