def sort_third(l: list):
    l_sorted = [x for i, x in enumerate(l) if i % 3 != 0]
    l_sorted += [sorted(y for y in l if i % 3 == 0)]
    return l_sorted