def exchange(lst1, lst2):
    even_lst = [x for x in lst1 if x % 2 == 0]
    return "YES" if len(even_lst) == len(lst1) else "NO"