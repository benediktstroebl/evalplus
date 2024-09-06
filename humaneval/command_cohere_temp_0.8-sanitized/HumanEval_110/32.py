def exchange(lst1, lst2):
    even_present = any(map(lambda x: x % 2 == 0, lst1))
    if even_present:
        return "YES"
    else: 
        return "NO"