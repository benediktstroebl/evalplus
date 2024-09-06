def sort_third(l: list):
    l_split = [x for i, x in enumerate(l) if i % 3 != 0]
    l_sorted = [x for i, x in enumerate(l) if i % 3 == 0]
    l_split = sorted(l_split)
    return l_split + l_sorted