def exchange(lst1, lst2):
    o = []
    e = []
    for i in lst1:
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)
    for i in lst2:
        if i % 2 == 0:
            o.append(i)
        else:
            e.append(i)
    if len(e) == 0:
        return "YES"
    else:
        return "NO"