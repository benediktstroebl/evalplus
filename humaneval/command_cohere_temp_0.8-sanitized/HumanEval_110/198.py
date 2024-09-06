def exchange(lst1, lst2):
    even_found = any(lst1)
    return "YES" if even_found and all(map(lambda x: x in lst2 or x in lst1, lst1)) else "NO"