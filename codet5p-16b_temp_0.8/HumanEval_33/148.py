

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    indices_not_div_by_3 = []
    indices_div_by_3 = []
    for i in range(len(l)):
        if i%3!= 0:
            indices_not_div_by_3.append(i)
        else:
            indices_div_by_3.append(i)
    indices_not_div_by_3.sort()
    indices_div_by_3.sort()
    third_list = []
    for i in range(len(indices_not_div_by_3)):
        third_list.append(l[indices_not_div_by_3[i]])
    for i in range(len(indices_div_by_3)):
        third_list.append(l[indices_div_by_3[i]])
    return third_list
    
    
