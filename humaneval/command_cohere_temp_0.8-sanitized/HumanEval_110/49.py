def exchange(lst1, lst2):
    even_occurrences = sum(x % 2 == 0 for x in lst1)
    total_occurrences = len(lst1)
    
    if even_occurrences == total_occurrences:
        return "YES"
    elif even_occurrences > total_occurrences:
        # More even numbers than odd in lst1, so we can take from lst2
        return "NO"
    else:
        # Odd numbers are more, so we can give to lst2 without any odd numbers left in lst1
        return "YES"