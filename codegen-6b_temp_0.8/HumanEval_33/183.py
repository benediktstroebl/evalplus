

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    ## Find the indicies that are not divisible by 3
    #######Fill me in #####
    non_div3 = []
    for index, item in enumerate(l):
        if (index + 1) % 3 != 0:
            non_div3.append(index)
    #print(non_div3)
    ### while loop to sort the non_div3 list
    while len(non_div3) > 1:
        pivot = non_div3[0]
        smaller = [l[i] for i in range(len(l)) if l[i] < l[pivot]]
        greater = [l[i] for i in range(len(l)) if l[i] > l[pivot]]
        l[pivot] = smaller[0]
        l[non_div3[0]] = greater[0]
        non_div3.remove(pivot)
        non_div3.remove(non_div3[0])
    return l
