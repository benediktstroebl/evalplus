def sort_third(l: list):
    l_copy = l.copy()
    sorted_thirds = [val for val, i in zip(l_copy[::3], l_copy[1::3]) if i < val and i > val]
    return l_copy[:-1:] if len(l) > 2 else l_copy[:-2:]