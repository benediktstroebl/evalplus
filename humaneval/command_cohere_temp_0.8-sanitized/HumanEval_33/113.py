def sort_third(l: list):
    l_copy = l.copy()
    sorted_thirds = [x for x in l if x % 3 == 0 and x not in l_copy]
    l_copy[:] = sorted(sorted_thirds)
    return l_copy