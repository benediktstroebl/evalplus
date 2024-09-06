def exchange(lst1, lst2):
    odd = lst1.count(2)
    even = lst2.count(2)
    if odd == 0 and even > 0:
        return "YES"
    elif even == 0 and odd > 0:
        return "NO"
    else:
        return "YES"