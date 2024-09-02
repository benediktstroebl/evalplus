

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    new_list = [0]*len(l)
    index = 0
    while index < len(l):
        new_list[index] = l[index]
        if index < len(l) - 1:
            if l[index+1] <= l[index]:
                new_list[index+1] = l[index+1]
                new_list[index] = l[index+1]
            else:
                new_list[index+1] = l[index]
                new_list[index] = l[index+1]
        index += 2
    return new_list

