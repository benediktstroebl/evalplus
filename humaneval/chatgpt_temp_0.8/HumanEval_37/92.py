def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    """
    even_items = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    result = [l[i] if i % 2 != 0 else even_items.pop(0) for i in range(len(l))]
    return result
