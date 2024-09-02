

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    if l == []:
        return []
    else:
        new_list = l[:]
        for i in range(len(new_list)):
            if i % 3 == 0:
                continue
            else:
                for j in range(len(new_list)):
                    if i == j:
                        continue
                    elif new_list[i] > new_list[j]:
                        temp = new_list[i]
                        new_list[i] = new_list[j]
                        new_list[j] = temp
        return new_list

