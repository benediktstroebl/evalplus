def total_match(lst1, lst2):
    total1 = sum(len(i) for i in lst1)
    total2 = sum(len(i) for i in lst2)
    
    if total1 < total2:
        return lst1
    elif total1 == total2:
        return lst1
    else:
        return lst2
