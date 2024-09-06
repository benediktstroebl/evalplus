def exchange(lst1, lst2):
    even_lst1 = [x for x in lst1 if x % 2 == 0]
    even_lst2 = [x for x in lst2 if x % 2 == 0]
    if len(even_lst1) == len(lst1) and len(even_lst2) == len(lst2):
        return "YES"
    return "NO"