

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Your code here
    even = l[::2]
    odd = l[1::2]

    sorted_even = sorted(even)

    # Your code here
    if len(sorted_even) > len(odd):
        sorted_even = sorted_even[:-1]

    l1 = []
    l2 = []
    for i in range(len(sorted_even)):
        l1.append(sorted_even[i])
        l1.append(odd[i])
    for i in range(len(odd) - len(sorted_even)):
        l2.append(odd[len(sorted_even) + i])

    return l1 + l2

