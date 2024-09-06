def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        try:
            temp = l[i:i+3]
            temp.sort()
            l_new.extend(temp)
        except:
            l_new.extend(l[i:i+3])
    return l_new