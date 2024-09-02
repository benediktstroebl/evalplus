

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # 1. initialize new list 
    new_list = []
    # 2. iterate thru l
    for i in l:
        # 3. add i to new_list if mod 3 == 0
        if i % 3 == 0:
            new_list.append(i)
    # 4. sort new_list
    new_list.sort()
    # 5. return new_list
    return new_list

