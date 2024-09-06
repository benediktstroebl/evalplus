def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    count_even_in_lst2 = any(map(lambda x: x % 2 == 0, lst2))
    if even_found and count_even_in_lst2:
        return "YES"
    return "NO"