def sort_third(l: list):
    l_copy = l.copy()
    return l_copy[:] [:: (len(l) + 1) % 3 != 0] + l_copy[:] [:: (len(l) + 1) % 3 == 0]