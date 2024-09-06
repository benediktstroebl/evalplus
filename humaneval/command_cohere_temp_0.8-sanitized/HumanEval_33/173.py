def sort_third(l: list):
    l_copy = l.copy()
    sorted_thirds = [val for ind, val in enumerate(l) if ind % 3 == 0 and val != l[ind]]
    sorted_thirds.sort()
    for i in range(0, len(l), 3):
        if i % 3 == 0:
            l[i] = sorted_thirds.pop(0)
    return l