def sort_third(l):
    l_copy = [i for i in l]
    sorted_l = [i for i in l if i%3 == 0]
    sorted_l.sort()
    for i in range(0, len(l), 3):
        l[i] = l_copy[i]
    for i in range(len(l)//3):
        l[i*3:i*3+3] = sorted_l[i:]
    return l