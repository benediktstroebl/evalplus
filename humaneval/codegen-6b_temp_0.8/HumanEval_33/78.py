

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    #your work here
    unsorted_list = []
    three_group_list = []
    third_list = []
    for x in l:
        unsorted_list.append(x)
        if x % 3 == 0:
            three_group_list.append(x)
            unsorted_list.remove(x)
    three_group_list = sorted(three_group_list)
    for x in unsorted_list:
        third_list.append(x)
    third_list = sorted(third_list)
    sorted_list = third_list + three_group_list
    return sorted_list

