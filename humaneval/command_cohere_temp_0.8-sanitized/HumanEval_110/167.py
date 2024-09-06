def exchange(lst1, lst2):
    if not lst1 or not lst2:
        return "Empty lists"
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
        elif x in lst2:
            lst2.remove(x)
    if odd:
        return "NO"
    elif len(lst2) == 0:
        return "YES"
    else:
        return "NO"