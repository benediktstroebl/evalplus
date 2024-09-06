def total_match(lst1, lst2):
    total1 = sum(len(str(el)) for el in lst1)
    total2 = sum(len(str(el)) for el in lst2)
    if total1 > total2:
        return lst1
    elif total2 > total1:
        return lst2
    else:
        return lst1 if len(lst1) < len(lst2) else lst2