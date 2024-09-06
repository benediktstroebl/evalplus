def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = True
            break
    if not odd:
        return "YES"
    else:
        temp = lst1
        lst1 = lst2
        lst2 = temp
        return "NO"