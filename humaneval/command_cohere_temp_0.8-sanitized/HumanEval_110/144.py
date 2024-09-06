def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    count_diff_odd = sum(1 for x in lst1 if x % 2 != 0) - sum(1 for x in lst2 if x % 2 != 0)
    
    if even_found and count_diff_odd == 0:
        return "YES"
    return "NO"