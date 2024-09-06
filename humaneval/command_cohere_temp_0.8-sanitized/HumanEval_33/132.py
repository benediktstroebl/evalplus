def sort_third(l):
    l3 = [ele for ele in l if ele % 3 == 0]
    l3.sort()
    return l3 + [ele for ele in l if ele % 3 != 0]