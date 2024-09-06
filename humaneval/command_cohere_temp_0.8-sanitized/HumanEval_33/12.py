def sort_third(l: list):
    l_copy = l.copy()
    sorted_third = [e for e in l if e % 3 == 0]
    sorted_third.sort()
    for e in l:
        if e % 3 == 0:
            l_copy[e // 3] = sorted_third[e // 3]
    return l_copy