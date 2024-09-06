def sort_third(l: list):
    l_copy = l.copy()
    return l_copy[:] [::3 == 0] + l_copy[:] [::3 == 1].sort() + l_copy[:] [::3 == 2]