def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
    if odd:
        return "NO"
    else:
        return "YES"