def sort_third(l: list):
    l_new = []
    for i in range(len(l)):
        if i%3 == 0:
            l_new.append(sorted([x for x in l if x==l[i]][0]))
        else:
            l_new.append(l[i])
    return l_new