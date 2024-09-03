def total_match(lst1, lst2):
    return lst1 if sum(1 for x in lst1 if x in lst2) > sum(1 for x in lst2 if x in lst1) else lst2