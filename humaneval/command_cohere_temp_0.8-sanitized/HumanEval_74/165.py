def total_match(lst1, lst2):
    # calculate the total char count in lst1 and lst2
    total1 = sum(len(el) for el in lst1)
    total2 = sum(len(el) for el in lst2)
    
    # check if total1 is less than total2
    if total1 < total2:
        return lst1
    elif total2 < total1:
        return lst2
    else:
        # if total is same, check if first list is lexically smaller, and return it if so
        if lst1 <= lst2:
            return lst1
        else:
            return lst2