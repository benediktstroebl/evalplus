def sort_third(l):
    l_copy = l.copy()
    return [l_copy[i] if i % 3 != 0 else sorted(l_copy[i::3]) for i in range(len(l))]