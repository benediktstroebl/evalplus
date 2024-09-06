def exchange(lst1, lst2):
    even_found = any(lst1)
    return "YES" if even_found and all(x in lst2 for x in lst1) else "NO"