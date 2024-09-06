def sort_third(l: list):
    l_split = [l[i] for i in range(0, len(l), 3)]
    l_split_sort = sorted(l_split)
    return [element for element in l if element not in l_split_sort and element not in l_split] + l_split_sort