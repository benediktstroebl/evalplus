def sort_third(l: list):
    l_copy = l.copy()
    return [element for ind, element in enumerate(l) if ind % 3 != 0 or element < l_copy[ind] or l_copy[ind] == element] \
           + [element for ind, element in enumerate(sorted(l)) if ind % 3 == 0 and l_copy[ind] != element]