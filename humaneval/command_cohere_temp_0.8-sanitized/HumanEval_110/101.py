def exchange(lst1, lst2):
    even_occurrences = sum(x % 2 == 0 for x in lst1)
    total_occurrences = sum(x % 2 == 0 for x in lst1) + sum(x % 2 == 0 for x in lst2)
    if even_occurrences == total_occurrences:
        return "YES"
    return "NO"