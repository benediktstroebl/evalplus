def total_match(lst1, lst2):
    # calculate the total length of strings in both lists
    total1 = sum(len(val) for val in lst1)
    total2 = sum(len(val) for val in lst2)

    # check if the length of strings in both lists are the same or not
    if total1 > total2:
        return lst1
    elif total2 > total1:
        return lst2
    else:
        # if the length is the same, return the first list or the list that appears first
        if lst1 == lst2:
            return lst1
        elif lst1[0] < lst2[0]:
            return lst1
        else:
            return lst2