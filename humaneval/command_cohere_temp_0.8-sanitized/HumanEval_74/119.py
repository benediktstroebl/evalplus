def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else max(set(lst1 + lst2), key=len)