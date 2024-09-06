

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    new_list = []
    for i in range(len(l)):
        if i % 2 == 0:
            new_list.append(l[i])
    new_list.sort()
    new_list2 = []
    for j in range(len(l)):
        if j % 2 == 1:
            new_list2.append(l[j])
    for k in range(len(new_list)):
        new_list2.insert(k * 2 + 1, new_list[k])
    return new_list2

