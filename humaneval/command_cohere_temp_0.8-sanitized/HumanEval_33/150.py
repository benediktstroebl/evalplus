def sort_third(l: list):
    l_split = [el for el in l if el%3 != 0]
    l_sorted = [el for el in l if el%3 == 0]
    l_sorted = sorted(l_sorted)
    return l_split + l_sorted