def total_match(lst1, lst2):
    # calculate the total char count in lst1 and lst2
    total1 = sum(len(el) for el in lst1)
    total2 = sum(len(el) for el in lst2)

    # check if the total char count is less in the first list
    if total1 > total2:
        return lst1
    elif total2 > total1:
        return lst2
    else:
        # if the totals are the same, return the first list
        return lst1