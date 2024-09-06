def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        try:
            temp = l[i:i+3]
            temp.sort()
            l_new += [x for x in temp]
        except:
            l_new.append(l[i])
    return l_new