def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    count_odd_in_lst2 = sum(map(lambda x: 1 if x % 2 != 0 else 0, lst2))
    return "YES" if even_found and count_odd_in_lst2 > 0 else "NO"