def exchange(lst1, lst2):
    even_exchange = False
    for x in lst1:
        if type(x) == int and x % 2 == 0:
            even_exchange = True
            break
    if even_exchange:
        for x in lst2:
            if type(x) == int and x % 2 != 0:
                lst1.append(x)
                lst2.remove(x)
    return "YES" if even_exchange else "NO"