def exchange(lst1, lst2):
    even_exchange = False
    for x in lst1:
        if type(x) == int and x % 2 == 0:
            even_exchange = True
            break
    if even_exchange:
        return "YES"
    else:
        return "NO"