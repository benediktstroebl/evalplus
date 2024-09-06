def total_match(lst1, lst2):
    l1,l2 = map(sum, (map(len, li) for li in (lst1, lst2))), len(lst2)
    return lst1 if l1 == l2 else lst2 if l1 > l2 else lst1