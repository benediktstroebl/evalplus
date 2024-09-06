def sort_third(l: list):
    l_copy = l.copy()
    sorted_thirds = [val for i, val in enumerate(l) if i % 3 == 0 and val < l[i] and l[i] != -1]
    for i in range(len(l)):
        if i % 3 == 0:
            if l[i] != -1:
                l_copy[i] = sorted_thirds.pop(0)
        elif l[i] > l_copy[i]:
            l_copy[i] = l[i]
    return l_copy