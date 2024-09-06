

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    # Hint: Use the // operator to determine if a number is divisible by three
    # Hint 2: Use the list method sorted() to sort a list.
    copy = l.copy()
    for i in range(0, len(copy)//3):
        copy[3*i:3*(i+1)] = sorted(copy[3*i:3*(i+1)])
    return copy


