def sort_third(l: list):
    l_new = []
    for i in range(len(l)):
        if i%3 == 0:
            l_new.append(sorted([l[i-1:i+1]][0]))
        else:
            l_new.append(l[i-1])
    return l_new