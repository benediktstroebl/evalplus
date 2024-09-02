

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    #create a new empty list to place the sorted values
    sorted_list = []

    #for each index pair in list
    for i, j in enumerate(l):
        #if the index is divisible by 2, add the value of the j'th index to sorted_list
        if i % 3 == 0:
            sorted_list.append(j)
        #if the index is divisible by 3, add the value of the j'th index to sorted_list
        if i % 3 == 1:
            sorted_list.append(j)
        #if the index is divisible by 2, add the value of the j'th index to sorted_list
        if i % 3 == 2:
            sorted_list.append(j)

    #return sorted_list
    return sorted_list


