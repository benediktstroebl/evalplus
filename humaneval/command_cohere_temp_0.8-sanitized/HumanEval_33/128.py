def sort_third(l: list):
    l_copy = l.copy()
    return l_copy[:][: len(l) // 3] + sorted(l_copy[:][len(l) // 3:]) + l_copy[:][-len(l) // 3 :]