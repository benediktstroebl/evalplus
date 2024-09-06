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
            res.append(x)
    return "NO"