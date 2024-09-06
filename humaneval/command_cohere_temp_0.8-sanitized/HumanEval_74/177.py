def total_match(lst1, lst2):
    l1, l2 = len(lst1[0]), len(lst2[0])
    for i in range(1, min(len(lst1), len(lst2))):
        if l1 + l2 != len(lst2[i]) + len(lst1[i]):
            return lst1 if l1 <= l2 else lst2
    return lst1 if l1 <= l2 else lst2