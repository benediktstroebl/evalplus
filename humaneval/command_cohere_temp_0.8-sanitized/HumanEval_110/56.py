def exchange(lst1, lst2):
    even_occurrences = sum(x % 2 == 0 for x in lst1)
    return "YES" if even_occurrences == len(lst1) else "NO"