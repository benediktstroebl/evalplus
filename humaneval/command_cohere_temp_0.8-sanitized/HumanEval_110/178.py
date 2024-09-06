def exchange(lst1, lst2):
    if not lst1 or not lst2:
        return "Error: Input lists are empty."
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
    return "YES" if not odd else "NO"