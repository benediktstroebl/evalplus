def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    count_diff_odd = sum(x % 2 != y % 2 for x, y in zip(lst1, lst2))
    return "YES" if even_found and count_diff_odd <= len(lst1) // 2 else "NO"