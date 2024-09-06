def total_match(lst1, lst2):
    l1, l2 = map(sum, (map(len, lst1), map(len, lst2))), sorted(lst1, key=len, reverse=True)
    return l2 if l1 == l2 else l1