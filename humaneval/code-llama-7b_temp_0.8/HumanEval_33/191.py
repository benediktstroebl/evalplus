

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    def sort_at_indices_not_divisible_by_three(l):
        indicies = [i for i in range(len(l)) if i % 3 != 0]
        return [l[i] for i in indicies]
    
    def sort_at_indices_divisible_by_three(l):
        indicies = [i for i in range(len(l)) if i % 3 == 0]
        return sorted([l[i] for i in indicies])
    
    return sort_at_indices_not_divisible_by_three(l) + sort_at_indices_divisible_by_three(l)

