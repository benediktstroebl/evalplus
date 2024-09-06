

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_list = []
    odd_list = []
    for i in l:
        if (l.index(i) % 2 == 0):
            even_list.append(i)
        else:
            odd_list.append(i)
    even_list.sort()
    index = 0
    while len(even_list) > 0:
        l.pop(index)
        l.insert(index, even_list.pop())
        index = index + 2
    index = 1
    while len(odd_list) > 0:
        l.pop(index)
        l.insert(index, odd_list.pop())
        index = index + 2
    return l
