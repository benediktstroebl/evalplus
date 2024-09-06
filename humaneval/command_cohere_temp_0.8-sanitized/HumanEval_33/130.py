def sort_third(l: list):
    l_split = [x for i, x in enumerate(l) if i % 3 == 0]
    l_sort = sorted(l_split)
    return l[:len(l_split)] + l_sort + l[len(l_split):]