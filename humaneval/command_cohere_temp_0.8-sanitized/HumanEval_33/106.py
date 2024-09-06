def sort_third(l):
    l3 = [ele for ind, ele in enumerate(l) if ind % 3 == 0]
    l3.sort()
    return l[:len(l3)] + [ele for ele in l if ind % 3 != 0]