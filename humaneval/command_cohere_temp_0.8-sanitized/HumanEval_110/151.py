def exchange(lst1, lst2):
    even_idx = [i for i, n in enumerate(lst1) if n % 2 == 0]
    if len(even_idx) == len(lst1):
        return "YES"
    else:
        return "NO"