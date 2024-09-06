def sort_third(l):
    l3 = [e for e in l if e%3 == 0]
    lX = [i for i in l if i%3 != 0]
    l3.sort()
    return lX + l3