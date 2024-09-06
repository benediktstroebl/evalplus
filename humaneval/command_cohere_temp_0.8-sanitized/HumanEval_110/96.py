def exchange(lst1, lst2):
    even_lst1 = [x for x in lst1 if x % 2 == 0]
    if len(even_lst1) != len(lst1):
        return "NO"
    else:
        return "YES"