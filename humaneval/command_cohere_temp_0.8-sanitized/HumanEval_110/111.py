def exchange(lst1, lst2):
    even_occurrences = sum(x % 2 == 0 for x in lst1)
    total_occurrences = len(lst1)
    
    if even_occurrences == total_occurrences:
        return "YES"
    elif even_occurrences > total_occurrences:
        # More even numbers than needed in lst1, can be transferred to lst2
        return "NO"
    else:
        # Check if there are enough even numbers in lst2 to fill lst1
        excess_even = total_occurrences - even_occurrences
        sufficient_even_in_lst2 = sum(x % 2 == 0 for x in lst2) >= excess_even
        if sufficient_even_in_lst2:
            return "YES"
        else:
            return "NO"