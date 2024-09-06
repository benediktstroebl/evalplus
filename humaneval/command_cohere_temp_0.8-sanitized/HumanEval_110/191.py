def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = True
            break
    
    if not odd:
        return "YES"
    
    res = lst1[:]
    for x in lst2:
        if x % 2:
            continue
        if x not in res:
            res.append(x)
    return "NO" if len(res) != len(lst1) else "YES"