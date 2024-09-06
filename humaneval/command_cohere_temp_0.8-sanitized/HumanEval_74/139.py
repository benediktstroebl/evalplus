def total_match(lst1, lst2):
    # calculate the total char count in lst1 and lst2
    total1 = sum(len(str(e)) for e in lst1)
    total2 = sum(len(str(e)) for e in lst2)
    
    # check if the total char count is less in the first list
    if total1 > total2:
        return lst1
    elif total1 < total2:
        return lst2
    else:
        # if char counts are the same, return the first list
        return lst1