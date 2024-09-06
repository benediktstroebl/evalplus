def exchange(lst1, lst2):
    even_occurrences = sum(x % 2 == 0 for x in lst1)
    total_occurrences = len(lst1)
    
    if even_occurrences == total_occurrences:
        return "YES"
    elif even_occurrences == 0:
        return "NO"
    else:
        # Try to find an even number in lst2 to exchange with an odd number in lst1
        for x in lst2:
            if x % 2 == 0:
                lst1.remove(x)
                lst2.remove(x)
                even_occurrences += 1
                total_occurrences -= 1
                if even_occurrences == total_occurrences:
                    return "YES"
                elif even_occurrences == 0:
                    return "NO"
        return "NO"