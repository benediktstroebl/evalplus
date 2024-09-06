def total_match(lst1, lst2):
    l1, l2 = len(lst1[0]), len(lst2[0])
    for i in range(min(len(lst1), len(lst2))):
        if l1 + l2 == sum(len(x) for x in lst2):
            return lst1
        if l2 + l1 == sum(len(x) for x in lst1):
            return lst2
    return lst1 if l1 <= l2 else lst2