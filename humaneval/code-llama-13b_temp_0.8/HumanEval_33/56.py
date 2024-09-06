

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
    list_one = []
    list_two = []
    #splits list l into 2 lists, one with odd indicies, one with even indicies
    for i in range(len(l)):
        if i % 2 == 0:
            list_one.append(l[i])
        else:
            list_two.append(l[i])
    #sorts list 2
    list_two = sorted(list_two)
    #adds 2 lists back together
    for i in range(len(list_two)):
        sorted_list.append(list_one[i])
        sorted_list.append(list_two[i])
    return sorted_list
