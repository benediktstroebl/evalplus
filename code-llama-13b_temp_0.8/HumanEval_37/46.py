

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even = []
    odd = []
    for i in range(len(l)):
        if i % 2 == 0:
            even.append(l[i])
        else:
            odd.append(l[i])
    sorted_even = sorted(even)
    even_index = 0
    odd_index = 0
    while even_index < len(sorted_even) and odd_index < len(odd):
        l[even_index * 2] = sorted_even[even_index]
        l[even_index * 2 + 1] = odd[odd_index]
        even_index += 1
        odd_index += 1
    return l
