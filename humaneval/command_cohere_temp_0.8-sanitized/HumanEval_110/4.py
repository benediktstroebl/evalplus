def exchange(lst1, lst2):
    even_exchange = False
    for x in lst1:
        if type(x) == int and x % 2 == 0:
            even_exchange = True
            break
    if even_exchange: 
        return "YES"
    else:
        li = 0
        for x in lst2:
            if type(x) == int and x % 2 == 0:
                li += 1
        if li == len(lst1):
            return "YES"
        else: 
            return "NO"