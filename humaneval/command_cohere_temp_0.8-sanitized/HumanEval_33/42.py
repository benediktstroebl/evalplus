def sort_third(l):
    l_copy = l.copy()
    return [i for i in l if i%3 != 0] + [sorted(x for x in l_copy if x%3 == 0)]