def total_match(lst1, lst2):
    l1,l2 = map(sum, (map(len, li) for li in (lst1, lst2))), sorted(lst1, key=len, reverse=True)
    return l2 if l1 >= l2[0] else l1