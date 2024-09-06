def sort_third(l: list):
    l_split = [sublist for sublist in l if len(sublist) == 3]
    l_sorted = [[val for val in sublist] for sublist in l_split]
    l_sorted = [val for sublist in l_sorted for val in sublist]
    return l_sorted