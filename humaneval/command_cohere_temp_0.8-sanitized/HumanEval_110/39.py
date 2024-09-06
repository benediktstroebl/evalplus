def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    return "YES" if even_found and all(map(lambda x: x in lst2, lst1)) else "NO"