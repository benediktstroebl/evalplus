def exchange(lst1, lst2):
    even_present = any(num % 2 == 0 for num in lst1)
    if even_present:
        return "YES"
    else:
        return "NO"