

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    length = len(l)
    sorted_list = []

    for i in range(0, length, 3):
        sorted_list.append(l[i])
        sorted_list.append(l[i+1])
        sorted_list.append(l[i+2])

    sorted_list.sort()

    new_list = []

    for i in range(length):
        if i % 3 == 0:
            new_list.append(sorted_list[0])
            sorted_list.pop(0)
        elif i % 3 == 1:
            new_list.append(sorted_list[1])
            sorted_list.pop(1)
        elif i % 3 == 2:
            new_list.append(sorted_list[2])
            sorted_list.pop(2)

    return new_list

