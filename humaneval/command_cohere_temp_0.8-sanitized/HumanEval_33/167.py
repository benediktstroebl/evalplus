def sort_third(l):
    l_copy = l.copy()
    return [item for i, item in enumerate(l) if i % 3 != 0] + [min(l_copy[i::3]) for i in range(int(len(l) / 3))]