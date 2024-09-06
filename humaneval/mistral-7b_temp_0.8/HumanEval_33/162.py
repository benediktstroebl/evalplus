

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # TODO: Write your function here
    # if you are stuck, read the docstrings for the built-in functions list(), list.sort(), and list.append
    # don't worry about testing your function - the tests below will take care of that for you
    l_ = list()
    for ind in range(len(l)):
        if ind % 3 == 0:
            l_.append(sorted(l[ind:ind+3])[0])
        else:
            l_.append(l[ind])
    return l_

