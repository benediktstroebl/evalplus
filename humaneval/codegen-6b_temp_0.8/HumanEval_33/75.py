

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # Your code here
    lst = list(l)
    lst_3 = []
    lst_1 = []
    lst_2 = []
    for i in lst:
        if i % 3 == 0:
            lst_3.append(i)
        elif i % 3 == 1:
            lst_1.append(i)
        elif i % 3 == 2:
            lst_2.append(i)

    lst_3.sort()
    lst_1.sort()
    lst_2.sort()

    lst_3.extend(lst_1)
    lst_3.extend(lst_2)
    return lst_3

