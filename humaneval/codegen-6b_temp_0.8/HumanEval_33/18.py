

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    #find indicies that I will use in the new sort list
    div3indices = [index for index,value in enumerate(l) if value%3 == 0]
    #find indicies that are not divisible by 3
    notdiv3indices = [index for index,value in enumerate(l) if value%3 != 0]
    #sort the values at the indicies that are not divisible by 3
    div3l = [item for index,item in enumerate(l) if index in div3indices]
    div3l.sort()
    #sort the values at the indicies that are divisible by 3
    notdiv3l = [item for index,item in enumerate(l) if index in notdiv3indices]
    notdiv3l.sort()
    #return a list of 4 values corresponding to the indices of l
    return div3l + notdiv3l
