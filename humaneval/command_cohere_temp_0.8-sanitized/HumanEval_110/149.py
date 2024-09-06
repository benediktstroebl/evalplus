def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = True
            break
    if odd:
        return "NO"
    for x in lst2:
        if x % 2:
            continue
        lst1.append(x)
        lst2.remove(x)
    return "YES"