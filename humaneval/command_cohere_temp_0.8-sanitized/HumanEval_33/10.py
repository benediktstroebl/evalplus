def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        tmp = l[i:i+3]
        tmp.sort()
        l_new.extend(tmp)
    return l_new