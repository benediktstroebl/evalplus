def exchange(lst1, lst2):
    odd = lst1.count(0)
    even = lst2.count(0)
    if odd == 0 and even > 0:
        return "YES"
    return "NO"