

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # Your code here
    def third(x):
        return x % 3 == 0

    def not_third(x):
        return x % 3!= 0

    sorted_l = l[:]
    sorted_l.sort()
    sorted_l = [sorted_l[i] if not_third(i) else l[i] for i in range(len(l))]
    return sorted_l
