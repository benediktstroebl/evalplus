def sort_third(l: list):
    l_copy = l.copy()
    sorted_thirds = [i for i in l if i % 3 == 0 and i in sorted(l_lcopy)]
    return l + sorted_thirds