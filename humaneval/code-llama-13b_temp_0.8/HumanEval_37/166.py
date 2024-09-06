

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    temp_list = []
    for i in range(0, len(l)):
        if i % 2 == 0:
            temp_list.append(l[i])
    temp_list.sort()
    output = []
    k = 0
    for j in range(0, len(l)):
        if j % 2 == 0:
            output.append(temp_list[k])
            k += 1
        else:
            output.append(l[j])
    return output
