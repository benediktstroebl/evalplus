def sort_third(l):
    l3 = [e for e in l if e[0] % 3 == 0]
    l3.sort()
    return l3 + [e for e in l if e[0] % 3 != 0]