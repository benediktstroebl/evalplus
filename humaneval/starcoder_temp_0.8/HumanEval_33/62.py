

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    if len(l) == 0:
        return []
    elif len(l) == 1:
        return l
    elif len(l) == 2:
        if l[0] > l[1]:
            return [l[1], l[0]]
        else:
            return l
    elif len(l) == 3:
        if l[0] > l[1]:
            return [l[1], l[0], l[2]]
        elif l[1] > l[2]:
            return [l[2], l[0], l[1]]
        else:
            return l
    else:
        new_list = []
        for i in range(len(l)):
            if i % 3 == 0:
                new_list.append(l[i])
            else:
                for j in range(len(new_list)):
                    if l[i] < new_list[j]:
                        new_list.insert(j, l[i])
                        break
        return new_list

