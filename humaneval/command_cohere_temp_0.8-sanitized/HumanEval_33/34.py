def sort_third(l: list):
    l_copy = l.copy()
    sorted_thirds = [y for x, y in enumerate(l) if x % 3 == 0 and y < l[x] // 3]
    for i in range(0, len(sorted_thirds), 2):
        l_copy[i] = sorted_thirds[i]
    for i in range(1, len(sorted_thirds), 2):
        l_copy[i] = sorted_thirds[i]
    return l_copy