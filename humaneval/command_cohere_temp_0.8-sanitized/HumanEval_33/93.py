def sort_third(l: list):
    l_copy = l.copy()
    return l_copy[:] [::3] + l_copy[:] [1::3] + l_copy[:] [2::3]