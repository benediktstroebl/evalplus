def sort_third(l):
    l_copy = [i for i in l]
    sorted_l = [i for i in l if i%3 == 0]
    sorted_l.sort()
    for i in range(len(l)):
        if i%3 == 0:
            l[i] = sorted_l[i//3]
        else:
            l[i] = l_copy[i]
    return l