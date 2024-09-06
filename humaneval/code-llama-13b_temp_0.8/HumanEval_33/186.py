

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    sorted_list = []
    l_index = 0
    while l_index < len(l):
        if l_index % 3 == 0:
            sorted_list.append(l[l_index])
            l_index += 1
        else:
            part_l = l[l_index:l_index+3]
            sorted_part = []
            for i in part_l:
                sorted_part.append(i)
            sorted_part.sort()
            for i in sorted_part:
                sorted_list.append(i)
            l_index += 3
    return sorted_list


