

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    def third(l: list):
        return l[2]
    
    def second(l: list):
        return l[1]
    
    def first(l: list):
        return l[0]

    new_list = l[:]
    new_list.sort(key=first)
    new_list.sort(key=second)
    new_list.sort(key=third)
    return new_list
