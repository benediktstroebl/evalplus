

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    # 1. Write a function that returns a list of thirds for a given list.
    def get_thirds(l):
        new_l = []
        for i in range(len(l)):
            if i % 3 != 0:
                new_l.append(l[i])
        return new_l

    # 2. Write a function that sorts a given list.
    def sort(l):
        l.sort()
        return l

    # 3. Put it all together!
    l_thirds = get_thirds(l)
    sorted_l = sort(l_thirds)
    l_sorted = [sorted_l[i] if i % 3 != 0 else l[i] for i in range(len(l))]
    return l_sorted

