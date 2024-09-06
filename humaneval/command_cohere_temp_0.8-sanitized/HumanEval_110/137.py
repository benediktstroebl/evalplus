def exchange(lst1, lst2):
    even_idx = [i for i, n in enumerate(lst1) if n % 2 == 0]
    if len(even_idx) != len(lst1):
        return "NO"
    lst1[even_idx], lst2[even_idx] = lst2[even_idx], lst1[even_idx]
    return "YES" if all(n % 2 == 0 for n in lst1) else "NO"