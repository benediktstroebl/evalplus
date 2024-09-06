def exchange(lst1, lst2):
    even_seen = False
    for elt in lst2:
        if not even_seen and elt % 2 == 0:
            even_seen = True
            continue
        if even_seen and elt % 2 != 0:
            return "NO"
    return "YES"