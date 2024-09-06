def exchange(lst1, lst2):
    even_occurring = any(x % 2 == 0 for x in lst1)
    if even_occurring and all(x % 2 == 0 for x in lst2):
        return "YES"
    return "NO"