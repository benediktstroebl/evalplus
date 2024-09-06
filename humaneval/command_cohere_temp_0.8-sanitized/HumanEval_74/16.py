def total_match(lst1, lst2):
    # calculate the total characters in all strings of the list
    total1 = sum(len(x) for x in lst1)
    total2 = sum(len(x) for x in lst2)
    
    # check if total1 is less than total2
    if total1 < total2:
        return lst1
    elif total2 < total1:
        return lst2
    else:
        # if total is same, return the first list
        return lst1