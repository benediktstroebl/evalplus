def total_match(lst1, lst2):
    # calculate the total char count in lst1 and lst2
    total1 = sum(len(str(e)) for e in lst1)
    total2 = sum(len(str(e)) for e in lst2)

    if total1 > total2:
        return lst2
    elif total2 > total1:
        return lst1
    else:
        return lst1 if len(lst1) < len(lst2) else lst2