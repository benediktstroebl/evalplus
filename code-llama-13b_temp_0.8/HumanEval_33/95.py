

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    "*** YOUR CODE HERE ***"
    index = 0
    while index < len(l):
        if index % 3 != 0:
            pass
        else:
            list_ = []
            list_.append(l[index])
            list_.append(l[index + 1])
            list_.append(l[index + 2])
            list_.sort()
            l[index] = list_[0]
            l[index + 1] = list_[1]
            l[index + 2] = list_[2]
        index += 1
    return l


