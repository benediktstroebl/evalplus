def sort_third(l: list):
    l_sorted = [el for ind, el in enumerate(l) if ind % 3 != 0]
    l_sorted += [sorted(el for el in l if ind % 3 == 0)]
    return l_sorted