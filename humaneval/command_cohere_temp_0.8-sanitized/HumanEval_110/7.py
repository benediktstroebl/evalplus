def exchange(lst1, lst2):
    even_occurrences = sum(x % 2 == 0 for x in lst1)
    total_occurrences = len(lst1)
    
    if even_occurrences == total_occurrences:
        return "YES"
    else:
        return "NO"